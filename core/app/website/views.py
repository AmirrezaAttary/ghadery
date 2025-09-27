from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.messages.views import SuccessMessageMixin
from .models import SMSNumber,PhoneNumber
from .forms import SMSNumberForm,PhoneNumberForm
# Create your views here.

class HomeView(TemplateView):
    template_name = "website/home.html"
    
    
class SMSNumberCreateView(SuccessMessageMixin,CreateView):
    model = SMSNumber
    form_class = SMSNumberForm
    template_name = "website/smsnumber_form.html"
    success_url = "/smsnumbers/"
    success_message = "شماره کاوه نگار با موفقیت ثبت شد."
    
    
class SMSNumberListView(ListView):
    model = SMSNumber
    template_name = "website/smsnumber_list.html"
    
    
    
class PhoneNumberCreateView(SuccessMessageMixin,CreateView):
    model = PhoneNumber
    form_class = PhoneNumberForm
    template_name = "website/phonenumber_form.html"
    success_url = "/phonenumbers/"
    success_message = "شماره موبایل با موفقیت ثبت شد."
    
    
class PhoneNumberListView(ListView):
    model = PhoneNumber
    template_name = "website/phonenumber_list.html"