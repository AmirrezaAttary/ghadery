from django import forms
from .models import DeviceReception


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