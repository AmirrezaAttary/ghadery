from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, ListView

from app.paziresh.models import DeviceReception
from app.website.models import SMSNumber

from .forms import SingleSMSForm, BulkSMSForm
from .models import SMSLog
from .services import send_sms, send_bulk_sms


class SMSDashboardView(LoginRequiredMixin, TemplateView):

    template_name = "sms/dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["ready_count"] = DeviceReception.objects.filter(
            status="ready"
        ).count()

        context["phone_count"] = SMSNumber.objects.count()

        context["sms_count"] = SMSLog.objects.count()

        return context


class ReadyDevicesView(LoginRequiredMixin, ListView):

    template_name = "sms/ready_devices.html"

    model = DeviceReception

    context_object_name = "devices"

    paginate_by = 20

    def get_queryset(self):

        return DeviceReception.objects.filter(
            status="ready"
        ).order_by("-id")


class SendReadyDeviceSMSView(LoginRequiredMixin, FormView):

    template_name = "sms/send_ready_device.html"

    def post(self, request, *args, **kwargs):

        device_id = kwargs.get("pk")

        try:

            device = DeviceReception.objects.get(
                pk=device_id,
                status="ready"
            )

        except DeviceReception.DoesNotExist:

            messages.error(
                request,
                "دستگاه مورد نظر پیدا نشد."
            )

            return self.redirect_to_ready()

        if not device.owner_phone:

            messages.error(
                request,
                "شماره موبایل مشتری ثبت نشده است."
            )

            return self.redirect_to_ready()

        message = (
            f"مشتری گرامی، "
            f"{device.device_name} شما آماده تحویل است. "
            f"لطفاً جهت دریافت دستگاه به مجموعه مراجعه فرمایید."
        )

        sender = SMSNumber.objects.first()

        sender_number = sender.number if sender else None

        result = send_sms(
            receptor=device.owner_phone,
            message=message,
            sender=sender_number,
        )

        if result["success"]:

            response = result.get("response")

            message_id = None

            if response:

                try:
                    message_id = str(response[0].messageid)

                except Exception:
                    pass

            SMSLog.objects.create(
                receptor=device.owner_phone,
                sender=sender_number,
                message=message,
                send_type="ready_device",
                status="success",
                message_id=message_id,
                sent_by=request.user,
            )

            messages.success(
                request,
                "پیام آماده تحویل با موفقیت ارسال شد."
            )

        else:

            SMSLog.objects.create(
                receptor=device.owner_phone,
                sender=sender_number,
                message=message,
                send_type="ready_device",
                status="failed",
                error_message=result["error"],
                sent_by=request.user,
            )

            messages.error(
                request,
                f"ارسال پیام ناموفق بود: {result['error']}"
            )

        return self.redirect_to_ready()

    def redirect_to_ready(self):

        from django.shortcuts import redirect

        return redirect("sms:ready-devices")


class SendSingleSMSView(LoginRequiredMixin, FormView):

    template_name = "sms/send_single.html"

    form_class = SingleSMSForm

    def form_valid(self, form):

        receptor = form.cleaned_data["receptor"]

        message = form.cleaned_data["message"]

        sender = form.cleaned_data["sender"]

        sender_number = sender.number if sender else None

        result = send_sms(
            receptor=receptor,
            message=message,
            sender=sender_number,
        )

        if result["success"]:

            response = result.get("response")

            message_id = None

            if response:

                try:
                    message_id = str(response[0].messageid)

                except Exception:
                    pass

            SMSLog.objects.create(
                receptor=receptor,
                sender=sender_number,
                message=message,
                send_type="single",
                status="success",
                message_id=message_id,
                sent_by=self.request.user,
            )

            messages.success(
                self.request,
                "پیامک با موفقیت ارسال شد."
            )

            form = SingleSMSForm()

            return self.render_to_response(
                self.get_context_data(
                    form=form
                )
            )

        SMSLog.objects.create(
            receptor=receptor,
            sender=sender_number,
            message=message,
            send_type="single",
            status="failed",
            error_message=result["error"],
            sent_by=self.request.user,
        )

        messages.error(
            self.request,
            f"ارسال پیامک ناموفق بود: {result['error']}"
        )

        return self.form_invalid(form)


class SendBulkSMSView(LoginRequiredMixin, FormView):

    template_name = "sms/send_bulk.html"

    form_class = BulkSMSForm

    def form_valid(self, form):

        phone_numbers = form.cleaned_data[
            "phone_numbers"
        ]

        message = form.cleaned_data[
            "message"
        ]

        sender = form.cleaned_data[
            "sender"
        ]

        sender_number = sender.number if sender else None

        receptors = [
            phone.tel
            for phone in phone_numbers
            if phone.tel
        ]

        result = send_bulk_sms(
            receptors=receptors,
            message=message,
            sender=sender_number,
        )

        if result["success"]:

            response = result.get("response")

            message_ids = []

            if response:

                try:

                    for item in response:
                        message_ids.append(
                            str(item.messageid)
                        )

                except Exception:
                    pass

            for index, receptor in enumerate(receptors):

                message_id = (
                    message_ids[index]
                    if index < len(message_ids)
                    else None
                )

                SMSLog.objects.create(
                    receptor=receptor,
                    sender=sender_number,
                    message=message,
                    send_type="bulk",
                    status="success",
                    message_id=message_id,
                    sent_by=self.request.user,
                )

            messages.success(
                self.request,
                f"پیامک با موفقیت برای {len(receptors)} شماره ارسال شد."
            )

        else:

            for receptor in receptors:

                SMSLog.objects.create(
                    receptor=receptor,
                    sender=sender_number,
                    message=message,
                    send_type="bulk",
                    status="failed",
                    error_message=result["error"],
                    sent_by=self.request.user,
                )

            messages.error(
                self.request,
                f"ارسال گروهی ناموفق بود: {result['error']}"
            )

        return self.form_invalid(form)


class SMSLogListView(LoginRequiredMixin, ListView):

    template_name = "sms/log_list.html"

    model = SMSLog

    context_object_name = "logs"

    paginate_by = 30

    def get_queryset(self):

        return SMSLog.objects.select_related(
            "sent_by"
        ).order_by("-id")

