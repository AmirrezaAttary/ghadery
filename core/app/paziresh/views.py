from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.views import View

from .models import DeviceReception, Warranty
from .forms import (
    DeviceReceptionForm,
    DeviceUpdateReceptionForm,
    WarrantyForm,
)


# =========================================================
# پذیرش دستگاه
# =========================================================

class PazireshListView(LoginRequiredMixin, ListView):
    template_name = "paziresh/list.html"
    model = DeviceReception
    paginate_by = 20

    def get_queryset(self):
        queryset = DeviceReception.objects.all()

        # ---------------- جستجو ----------------
        search_q = self.request.GET.get("q", "").strip()

        if search_q:
            queryset = queryset.filter(
                Q(id__icontains=search_q) |
                Q(device_name__icontains=search_q) |
                Q(device_model__icontains=search_q) |
                Q(device_serial__icontains=search_q) |
                Q(owner_name__icontains=search_q) |
                Q(owner_phone__icontains=search_q) |
                Q(owner_national_id__icontains=search_q)
            )

        # ---------------- فیلتر وضعیت ----------------
        status = self.request.GET.get("status")

        if status in ["repairing", "ready", "delivered"]:
            queryset = queryset.filter(status=status)

        return queryset


# =========================================================
# ثبت پذیرش دستگاه
# =========================================================

class PazireshCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    template_name = "paziresh/create.html"
    model = DeviceReception
    form_class = DeviceReceptionForm
    success_url = "/paziresh/list/"
    success_message = "دستگاه با موفقیت پذیرش شد."

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        # وضعیت اولیه دستگاه
        form.instance.status = "repairing"

        return super().form_valid(form)


# =========================================================
# ویرایش پذیرش
# =========================================================

class PazireshUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    template_name = "paziresh/update.html"
    model = DeviceReception
    form_class = DeviceUpdateReceptionForm
    success_url = "/paziresh/list/"
    success_message = "دستگاه با موفقیت ویرایش شد."

    def form_valid(self, form):
        old_status = self.get_object().status
        new_status = form.cleaned_data.get("status")

        # اگر دستگاه تحویل داده شده است
        if new_status == "delivered":

            # زمان تحویل را ثبت کن
            if not self.object.exit_date:
                from django.utils import timezone
                form.instance.exit_date = timezone.now()

        else:
            # اگر دوباره از حالت تحویل خارج شد
            form.instance.exit_date = None

        return super().form_valid(form)


# =========================================================
# فاکتور پذیرش
# =========================================================

class PazireshFaktorDetail(LoginRequiredMixin, DetailView):
    template_name = "paziresh/faktor.html"
    model = DeviceReception


# =========================================================
# استعلام مشتری بر اساس کد ملی
# =========================================================

class PazireshInquiryView(LoginRequiredMixin, View):

    def get(self, request):
        national_id = request.GET.get(
            "national_id",
            ""
        ).strip()

        if not national_id:
            return JsonResponse({
                "found": False,
                "message": "کد ملی وارد نشده است."
            })

        reception = (
            DeviceReception.objects
            .filter(owner_national_id=national_id)
            .order_by("-id")
            .first()
        )

        if not reception:
            return JsonResponse({
                "found": False,
                "message": "سابقه‌ای برای این کد ملی یافت نشد."
            })

        data = {
            "owner_name": reception.owner_name,
            "owner_phone": reception.owner_phone,
            "owner_landline": reception.owner_landline or "",
            "owner_address": reception.owner_address,
        }

        return JsonResponse({
            "found": True,
            "data": data
        })


# =========================================================
# لیست گارانتی‌ها
# =========================================================

class WarrantyListView(LoginRequiredMixin, ListView):
    template_name = "paziresh/warranty_list.html"
    model = Warranty
    paginate_by = 20

    def get_queryset(self):
        queryset = Warranty.objects.select_related(
            "device"
        ).all()

        search_q = self.request.GET.get(
            "q",
            ""
        ).strip()

        if search_q:
            queryset = queryset.filter(
                Q(id__icontains=search_q) |
                Q(device__device_name__icontains=search_q) |
                Q(device__device_model__icontains=search_q) |
                Q(device__device_serial__icontains=search_q) |
                Q(device__owner_name__icontains=search_q) |
                Q(device__owner_national_id__icontains=search_q) |
                Q(device__owner_phone__icontains=search_q)
            )

        return queryset


# =========================================================
# ایجاد گارانتی
# =========================================================

class WarrantyCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    template_name = "paziresh/warranty_create.html"
    model = Warranty
    form_class = WarrantyForm
    success_url = "/paziresh/warranty/list/"
    success_message = "گارانتی با موفقیت ثبت شد."

    def form_valid(self, form):
        form.instance.issued_by = self.request.user

        return super().form_valid(form)


# =========================================================
# ویرایش گارانتی
# =========================================================

class WarrantyUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    template_name = "paziresh/warranty_create.html"
    model = Warranty
    form_class = WarrantyForm
    success_url = "/paziresh/warranty/list/"
    success_message = "گارانتی با موفقیت ویرایش شد."


# =========================================================
# چاپ گارانتی
# =========================================================

class WarrantyPrintDetail(
    LoginRequiredMixin,
    DetailView
):
    template_name = "paziresh/warranty_print.html"
    model = Warranty

