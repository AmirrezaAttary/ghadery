from django import forms

from app.website.models import SMSNumber, PhoneNumber


class SenderMixin:

    def add_sender_field(self):

        self.fields["sender"] = forms.ModelChoiceField(
            queryset=SMSNumber.objects.all(),
            required=False,
            label="شماره ارسال کننده",
            empty_label="شماره پیش‌فرض کاوه نگار",
            widget=forms.Select(
                attrs={
                    "class": "form-input"
                }
            )
        )


class SingleSMSForm(SenderMixin, forms.Form):

    sender = forms.ModelChoiceField(
        queryset=SMSNumber.objects.all(),
        required=False,
        label="شماره ارسال کننده",
        empty_label="شماره پیش‌فرض کاوه نگار",
        widget=forms.Select(
            attrs={
                "class": "form-input"
            }
        )
    )

    receptor = forms.CharField(
        max_length=12,
        label="شماره گیرنده",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "09123456789",
                "dir": "ltr",
            }
        )
    )

    message = forms.CharField(
        label="متن پیام",
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "rows": 6,
                "placeholder": "متن پیام را وارد کنید..."
            }
        )
    )

    def clean_receptor(self):

        number = self.cleaned_data["receptor"].strip()

        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        english_digits = "0123456789"

        number = number.translate(
            str.maketrans(
                persian_digits,
                english_digits
            )
        )

        if not number.startswith("09"):
            raise forms.ValidationError(
                "شماره موبایل باید با 09 شروع شود."
            )

        if len(number) != 11:
            raise forms.ValidationError(
                "شماره موبایل باید ۱۱ رقم باشد."
            )

        if not number.isdigit():
            raise forms.ValidationError(
                "شماره موبایل معتبر نیست."
            )

        return number


class BulkSMSForm(forms.Form):

    sender = forms.ModelChoiceField(
        queryset=SMSNumber.objects.all(),
        required=False,
        label="شماره ارسال کننده",
        empty_label="شماره پیش‌فرض کاوه نگار",
        widget=forms.Select(
            attrs={
                "class": "form-input"
            }
        )
    )

    phone_numbers = forms.ModelMultipleChoiceField(
        queryset=PhoneNumber.objects.filter(
            tel__isnull=False
        ).exclude(
            tel=""
        ),
        required=True,
        label="شماره‌های گیرنده",
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-input",
                "size": 15,
            }
        )
    )

    message = forms.CharField(
        label="متن پیام",
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "rows": 6,
                "placeholder": "متن پیام را وارد کنید..."
            }
        )
    )

