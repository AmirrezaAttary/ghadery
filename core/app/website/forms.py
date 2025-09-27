from django.forms import ModelForm
from .models import SMSNumber,PhoneNumber

class SMSNumberForm(ModelForm):
    class Meta:
        model = SMSNumber
        fields = ['number']
        
        
class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['tel']