from django import forms
from django.db.models import Q
from .models import DeviceReception, Warranty
import jdatetime



class DeviceReceptionForm(forms.ModelForm):
    class Meta:
        model = DeviceReception
        fields = [
            # device information
            "device_name",
            "device_type",
            "device_model",
            "device_serial",
            # reception information
            "owner_name",
            "owner_phone",
            "owner_national_id",
            "owner_landline",
            "owner_address",
            # other information
            "appearance_issue",
            "description",
            "technician_note",
            "cost",
            "has_warranty",
            "warranty_period",
            "created_by",
            # new fields
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
            "created_by": "ثبت شده توسط",
            "reception_type": "نوع پذیرش",
            "delivery_type": "نوع تحویل",
        }
        widgets = {
            "exit_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "owner_address": forms.Textarea(attrs={"rows": 3}),
            "appearance_issue": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "technician_note": forms.Textarea(attrs={"rows": 3}),
            "reception_type": forms.RadioSelect,
            "delivery_type": forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # device information
        for field in ['device_name', 'device_type', 'device_model', 'device_serial']:
            self.fields[field].widget.attrs['class'] = 'form-input'
        # reception information
        for field in ['owner_name', 'owner_phone', 'owner_national_id', 'owner_landline', 'owner_address']:
            self.fields[field].widget.attrs['class'] = 'form-input'
        # other information
        for field in ['appearance_issue', 'description', 'technician_note', 'cost', 'warranty_period', 'created_by']:
            self.fields[field].widget.attrs['class'] = 'form-input'
        self.fields['has_warranty'].widget.attrs['class'] = 'form-checkbox'
        # new fields
        self.fields['reception_type'].widget.attrs['class'] = 'form-radio'
        self.fields['delivery_type'].widget.attrs['class'] = 'form-radio'


class DeviceUpdateReceptionForm(forms.ModelForm):
    class Meta:
        model = DeviceReception
        fields = [
            "exit_date",
            "is_ready",
            # device information
            "device_name",
            "device_type",
            "device_model",
            "device_serial",
            # reception information
            "owner_name",
            "owner_phone",
            "owner_national_id",
            "owner_landline",
            "owner_address",
            # other information
            "appearance_issue",
            "description",
            "technician_note",
            "cost",
            "has_warranty",
            "warranty_period",
            # new fields
            "reception_type",
            "delivery_type",
        ]
        widgets = {
            "exit_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "owner_address": forms.Textarea(attrs={"rows": 3}),
            "appearance_issue": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "technician_note": forms.Textarea(attrs={"rows": 3}),
            "reception_type": forms.RadioSelect,
            "delivery_type": forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # device information
        for field in ['device_name', 'device_type', 'device_model', 'device_serial']:
            self.fields[field].widget.attrs['class'] = 'form-input'
        # reception information
        for field in ['owner_name', 'owner_phone', 'owner_national_id', 'owner_landline', 'owner_address']:
            self.fields[field].widget.attrs['class'] = 'form-input'
        # other information
        for field in ['appearance_issue', 'description', 'technician_note', 'cost', 'warranty_period']:
            self.fields[field].widget.attrs['class'] = 'form-input'
        self.fields['has_warranty'].widget.attrs['class'] = 'form-checkbox'
        self.fields['exit_date'].widget.attrs['class'] = 'form-input'
        self.fields['is_ready'].widget.attrs['class'] = 'form-checkbox'
        # new fields
        self.fields['reception_type'].widget.attrs['class'] = 'form-radio'
        self.fields['delivery_type'].widget.attrs['class'] = 'form-radio'





class WarrantyForm(forms.ModelForm):
    start_date = forms.CharField(
        label="تاریخ شروع گارانتی",
        widget=forms.TextInput(attrs={
            'class': 'form-input jalali-datepicker',
            'placeholder': '۱۴۰۳/۰۱/۰۱',
            'autocomplete': 'off',
        })
    )
    end_date = forms.CharField(
        label="تاریخ پایان گارانتی",
        widget=forms.TextInput(attrs={
            'class': 'form-input jalali-datepicker',
            'placeholder': '۱۴۰۳/۰۷/۰۱',
            'autocomplete': 'off',
        })
    )

    class Meta:
        model = Warranty
        fields = ['device', 'description', 'start_date', 'end_date']
        labels = {
            'device': 'دستگاه (پذیرش)',
            'description': 'توضیحات گارانتی',
        }
        widgets = {
            'device': forms.Select(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # فقط دستگاه‌هایی که واقعاً گارانتی دارن و قبلاً گارانتی براشون ثبت نشده
        queryset = DeviceReception.objects.filter(has_warranty=True).exclude(
            warranties__isnull=False
        )

        if self.instance and self.instance.pk:
            queryset = DeviceReception.objects.filter(
                Q(pk=self.instance.device_id) | Q(pk__in=queryset.values_list('pk', flat=True))
            )

        self.fields['device'].queryset = queryset.order_by('-id')
        self.fields['device'].empty_label = "— انتخاب دستگاه —"

        # موقع ویرایش، تاریخ‌های میلادی ذخیره‌شده رو به شمسی تبدیل کن تا توی فرم نمایش داده بشه
        if self.instance and self.instance.pk:
            if self.instance.start_date:
                self.initial['start_date'] = jdatetime.date.fromgregorian(
                    date=self.instance.start_date
                ).strftime('%Y/%m/%d')
            if self.instance.end_date:
                self.initial['end_date'] = jdatetime.date.fromgregorian(
                    date=self.instance.end_date
                ).strftime('%Y/%m/%d')

    @staticmethod
    def _to_gregorian(value):
        value = value.strip().replace('-', '/')
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        english_digits = '0123456789'
        value = value.translate(str.maketrans(persian_digits, english_digits))

        parts = value.split('/')
        if len(parts) != 3:
            raise forms.ValidationError("فرمت تاریخ باید به صورت ۱۴۰۳/۰۱/۰۱ باشد.")
        try:
            y, m, d = (int(p) for p in parts)
            return jdatetime.date(y, m, d).togregorian()
        except ValueError:
            raise forms.ValidationError("تاریخ وارد شده معتبر نیست.")

    def clean_start_date(self):
        return self._to_gregorian(self.cleaned_data['start_date'])

    def clean_end_date(self):
        return self._to_gregorian(self.cleaned_data['end_date'])

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        if start and end and end < start:
            raise forms.ValidationError("تاریخ پایان گارانتی نمی‌تواند قبل از تاریخ شروع باشد.")
        return cleaned_data