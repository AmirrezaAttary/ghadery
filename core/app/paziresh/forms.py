from django import forms
from django.db.models import Q
from .models import DeviceReception, Warranty

import jdatetime


# =========================================================
# فرم ثبت پذیرش دستگاه
# =========================================================

class DeviceReceptionForm(forms.ModelForm):

    class Meta:
        model = DeviceReception

        fields = [
            # ---------------- مشخصات دستگاه ----------------
            "device_name",
            "device_type",
            "device_model",
            "device_serial",

            # ---------------- مشخصات مالک ----------------
            "owner_name",
            "owner_phone",
            "owner_national_id",
            "owner_landline",
            "owner_address",

            # ---------------- اطلاعات تعمیر ----------------
            "appearance_issue",
            "description",
            "technician_note",
            "cost",

            # ---------------- گارانتی ----------------
            "has_warranty",
            "warranty_period",

            # ---------------- نوع پذیرش و تحویل ----------------
            "reception_type",
            "delivery_type",
        ]

        labels = {
            "device_name": "نام دستگاه",
            "device_type": "نوع دستگاه",
            "device_model": "مدل دستگاه",
            "device_serial": "سریال دستگاه",

            "owner_name": "نام مالک",
            "owner_phone": "شماره تماس",
            "owner_national_id": "کد ملی",
            "owner_landline": "تلفن ثابت",
            "owner_address": "آدرس",

            "appearance_issue": "ایراد ظاهری",
            "description": "توضیحات",
            "technician_note": "نظر تکنسین",
            "cost": "هزینه",

            "has_warranty": "گارانتی",
            "warranty_period": "مدت گارانتی (ماه)",

            "reception_type": "نوع پذیرش",
            "delivery_type": "نوع تحویل",
        }

        widgets = {
            "owner_address": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),

            "appearance_issue": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),

            "technician_note": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),

            "reception_type": forms.RadioSelect,

            "delivery_type": forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ---------------- مشخصات دستگاه ----------------

        for field in [
            "device_name",
            "device_type",
            "device_model",
            "device_serial",
        ]:
            self.fields[field].widget.attrs["class"] = "form-input"

        # ---------------- مشخصات مالک ----------------

        for field in [
            "owner_name",
            "owner_phone",
            "owner_national_id",
            "owner_landline",
            "owner_address",
        ]:
            self.fields[field].widget.attrs["class"] = "form-input"

        # ---------------- اطلاعات تعمیر ----------------

        for field in [
            "appearance_issue",
            "description",
            "technician_note",
            "cost",
            "warranty_period",
        ]:
            self.fields[field].widget.attrs["class"] = "form-input"

        # ---------------- گارانتی ----------------

        self.fields["has_warranty"].widget.attrs["class"] = "form-checkbox"

        # ---------------- نوع پذیرش و تحویل ----------------

        self.fields["reception_type"].widget.attrs["class"] = "form-radio"
        self.fields["delivery_type"].widget.attrs["class"] = "form-radio"


# =========================================================
# فرم ویرایش پذیرش دستگاه
# =========================================================



class DeviceUpdateReceptionForm(forms.ModelForm):

    # ---------------- تاریخ خروج ----------------

    exit_date = forms.CharField(
        required=False,
        label="تاریخ خروج",
        widget=forms.TextInput(
            attrs={
                "class": "form-input jalali-datepicker",
                "placeholder": "۱۴۰۵/۰۵/۱۶ ۱۶:۳۰",
                "autocomplete": "off",
                "readonly": "readonly",
            }
        )
    )

    class Meta:
        model = DeviceReception

        fields = [
            "exit_date",
            "status",

            # مشخصات دستگاه
            "device_name",
            "device_type",
            "device_model",
            "device_serial",

            # مشخصات مالک
            "owner_name",
            "owner_phone",
            "owner_national_id",
            "owner_landline",
            "owner_address",

            # مشخصات مشکل
            "appearance_issue",
            "description",
            "technician_note",
            "cost",

            # گارانتی
            "has_warranty",
            "warranty_period",

            # نوع پذیرش و تحویل
            "reception_type",
            "delivery_type",
        ]

        labels = {
            "exit_date": "تاریخ خروج",
            "status": "وضعیت دستگاه",

            "device_name": "نام دستگاه",
            "device_type": "نوع دستگاه",
            "device_model": "مدل دستگاه",
            "device_serial": "سریال دستگاه",

            "owner_name": "نام مالک",
            "owner_phone": "شماره تماس",
            "owner_national_id": "کد ملی",
            "owner_landline": "تلفن ثابت",
            "owner_address": "آدرس",

            "appearance_issue": "ایراد ظاهری",
            "description": "توضیحات",
            "technician_note": "نظر تکنسین",
            "cost": "هزینه",

            "has_warranty": "گارانتی",
            "warranty_period": "مدت گارانتی (ماه)",

            "reception_type": "نوع پذیرش",
            "delivery_type": "نوع تحویل",
        }

        widgets = {
            "owner_address": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-input",
                }
            ),

            "appearance_issue": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-input",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-input",
                }
            ),

            "technician_note": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-input",
                }
            ),

            "reception_type": forms.RadioSelect,

            "delivery_type": forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # ---------------- مشخصات دستگاه ----------------

        for field in [
            "device_name",
            "device_type",
            "device_model",
            "device_serial",
        ]:
            self.fields[field].widget.attrs["class"] = "form-input"

        # ---------------- مشخصات مالک ----------------

        for field in [
            "owner_name",
            "owner_phone",
            "owner_national_id",
            "owner_landline",
            "owner_address",
        ]:
            self.fields[field].widget.attrs["class"] = "form-input"

        # ---------------- مشخصات مشکل ----------------

        for field in [
            "appearance_issue",
            "description",
            "technician_note",
            "cost",
            "warranty_period",
        ]:
            self.fields[field].widget.attrs["class"] = "form-input"

        # ---------------- وضعیت ----------------

        self.fields["status"].widget.attrs["class"] = "form-input"

        # ---------------- گارانتی ----------------

        self.fields["has_warranty"].widget.attrs["class"] = "form-checkbox"

        # ---------------- نوع پذیرش و تحویل ----------------

        self.fields["reception_type"].widget.attrs["class"] = "form-radio"

        self.fields["delivery_type"].widget.attrs["class"] = "form-radio"

        # ---------------- نمایش تاریخ خروج ----------------

        if self.instance and self.instance.pk and self.instance.exit_date:

            self.initial["exit_date"] = (
                jdatetime.datetime.fromgregorian(
                    datetime=self.instance.exit_date
                ).strftime("%Y/%m/%d %H:%M")
            )

    # ==================================================
    # تبدیل تاریخ شمسی به میلادی
    # ==================================================

    @staticmethod
    def _to_gregorian_datetime(value):

        value = value.strip()

        # تبدیل اعداد فارسی به انگلیسی
        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        english_digits = "0123456789"

        value = value.translate(
            str.maketrans(
                persian_digits,
                english_digits
            )
        )

        # تبدیل - به /
        value = value.replace("-", "/")

        try:

            # ------------------------------------------
            # تاریخ + ساعت
            # مثال:
            # 1405/05/16 16:30
            # ------------------------------------------

            if " " in value:

                date_part, time_part = value.split()

                year, month, day = map(
                    int,
                    date_part.split("/")
                )

                hour, minute = map(
                    int,
                    time_part.split(":")
                )

            # ------------------------------------------
            # فقط تاریخ
            # مثال:
            # 1405/05/16
            # ------------------------------------------

            else:

                date_part = value

                year, month, day = map(
                    int,
                    date_part.split("/")
                )

                # اگر ساعت ارسال نشده باشد
                # ساعت پیش‌فرض 00:00 است.

                hour = 0
                minute = 0

            return jdatetime.datetime(
                year,
                month,
                day,
                hour,
                minute
            ).togregorian()

        except (ValueError, TypeError):

            raise forms.ValidationError(
                "فرمت تاریخ باید به صورت ۱۴۰۵/۰۵/۱۶ ۱۶:۳۰ باشد."
            )

    # ==================================================
    # اعتبارسنجی تاریخ خروج
    # ==================================================

    def clean_exit_date(self):

        value = self.cleaned_data.get("exit_date")

        if not value:
            return None

        return self._to_gregorian_datetime(value)


# =========================================================
# فرم گارانتی
# =========================================================

class WarrantyForm(forms.ModelForm):

    start_date = forms.CharField(
        label="تاریخ شروع گارانتی",
        widget=forms.TextInput(
            attrs={
                "class": "form-input jalali-datepicker",
                "placeholder": "۱۴۰۳/۰۱/۰۱",
                "autocomplete": "off",
            }
        )
    )

    end_date = forms.CharField(
        label="تاریخ پایان گارانتی",
        widget=forms.TextInput(
            attrs={
                "class": "form-input jalali-datepicker",
                "placeholder": "۱۴۰۳/۰۷/۰۱",
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = Warranty

        fields = [
            "device",
            "description",
            "start_date",
            "end_date",
        ]

        labels = {
            "device": "دستگاه (پذیرش)",
            "description": "توضیحات گارانتی",
        }

        widgets = {
            "device": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 4,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # فقط دستگاه‌هایی که:
        # 1. گارانتی دارند
        # 2. هنوز برای آنها گارانتی ثبت نشده
        queryset = (
            DeviceReception.objects
            .filter(has_warranty=True)
            .exclude(warranties__isnull=False)
        )

        # هنگام ویرایش گارانتی،
        # دستگاه فعلی هم باید در لیست نمایش داده شود.
        if self.instance and self.instance.pk:
            queryset = DeviceReception.objects.filter(
                Q(pk=self.instance.device_id) |
                Q(
                    pk__in=queryset.values_list(
                        "pk",
                        flat=True
                    )
                )
            )

        self.fields["device"].queryset = queryset.order_by("-id")

        self.fields["device"].empty_label = "— انتخاب دستگاه —"

        # ---------------- تبدیل تاریخ میلادی به شمسی ----------------

        if self.instance and self.instance.pk:

            if self.instance.start_date:
                self.initial["start_date"] = (
                    jdatetime.date.fromgregorian(
                        date=self.instance.start_date
                    ).strftime("%Y/%m/%d")
                )

            if self.instance.end_date:
                self.initial["end_date"] = (
                    jdatetime.date.fromgregorian(
                        date=self.instance.end_date
                    ).strftime("%Y/%m/%d")
                )

    # =====================================================
    # تبدیل تاریخ شمسی به میلادی
    # =====================================================

    @staticmethod
    def _to_gregorian(value):

        value = value.strip().replace("-", "/")

        # تبدیل اعداد فارسی به انگلیسی
        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        english_digits = "0123456789"

        value = value.translate(
            str.maketrans(
                persian_digits,
                english_digits
            )
        )

        parts = value.split("/")

        if len(parts) != 3:
            raise forms.ValidationError(
                "فرمت تاریخ باید به صورت ۱۴۰۳/۰۱/۰۱ باشد."
            )

        try:
            year, month, day = (
                int(part)
                for part in parts
            )

            return jdatetime.date(
                year,
                month,
                day
            ).togregorian()

        except ValueError:
            raise forms.ValidationError(
                "تاریخ وارد شده معتبر نیست."
            )

    # =====================================================
    # تاریخ شروع
    # =====================================================

    def clean_start_date(self):

        value = self.cleaned_data.get("start_date")

        if not value:
            raise forms.ValidationError(
                "تاریخ شروع گارانتی الزامی است."
            )

        return self._to_gregorian(value)

    # =====================================================
    # تاریخ پایان
    # =====================================================

    def clean_end_date(self):

        value = self.cleaned_data.get("end_date")

        if not value:
            raise forms.ValidationError(
                "تاریخ پایان گارانتی الزامی است."
            )

        return self._to_gregorian(value)

    # =====================================================
    # اعتبارسنجی تاریخ‌ها
    # =====================================================

    def clean(self):

        cleaned_data = super().clean()

        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")

        if start and end and end < start:
            raise forms.ValidationError(
                "تاریخ پایان گارانتی نمی‌تواند قبل از تاریخ شروع باشد."
            )

        return cleaned_data

