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
        ]
        widgets = {
            "exit_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "owner_address": forms.Textarea(attrs={"rows": 3}),
            "appearance_issue": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "technician_note": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # device information
        self.fields['device_name'].widget.attrs['class'] = 'form-input'
        self.fields['device_type'].widget.attrs['class'] = 'form-input'
        self.fields['device_model'].widget.attrs['class'] = 'form-input'
        self.fields['device_serial'].widget.attrs['class'] = 'form-input'
        # reception information
        self.fields['owner_name'].widget.attrs['class'] = 'form-input'
        self.fields['owner_phone'].widget.attrs['class'] = 'form-input'
        self.fields['owner_national_id'].widget.attrs['class'] = 'form-input'
        self.fields['owner_landline'].widget.attrs['class'] = 'form-input'
        self.fields['owner_address'].widget.attrs['class'] = 'form-input'
        # other information
        self.fields['appearance_issue'].widget.attrs['class'] = 'form-input'
        self.fields['description'].widget.attrs['class'] = 'form-input'
        self.fields['technician_note'].widget.attrs['class'] = 'form-input'
        self.fields['cost'].widget.attrs['class'] = 'form-input'
        self.fields['has_warranty'].widget.attrs['class'] = 'form-checkbox'
        self.fields['warranty_period'].widget.attrs['class'] = 'form-input'
        self.fields['created_by'].widget.attrs['class'] = 'form-input'