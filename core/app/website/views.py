from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from .models import SMSNumber,PhoneNumber
from .forms import SMSNumberForm,PhoneNumberForm
# Create your views here.

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "website/home.html"
    
    
class SMSNumberCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = SMSNumber
    form_class = SMSNumberForm
    template_name = "website/smsnumber_form.html"
    success_url = "/smsnumbers/"
    success_message = "شماره کاوه نگار با موفقیت ثبت شد."
    
    
class SMSNumberListView(ListView):
    model = SMSNumber
    template_name = "website/smsnumber_list.html"
    
    def get_queryset(self):
        queryset = SMSNumber.objects.all()
        search_q = self.request.GET.get('q')
        
        if search_q:
            queryset = queryset.filter(number__icontains=search_q)

        return queryset
    
    
    
class PhoneNumberCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = PhoneNumber
    form_class = PhoneNumberForm
    template_name = "website/phonenumber_form.html"
    success_url = "/phonenumbers/"
    success_message = "شماره موبایل با موفقیت ثبت شد."
    
    
class PhoneNumberListView(LoginRequiredMixin,ListView):
    model = PhoneNumber
    template_name = "website/phonenumber_list.html"

    def get_queryset(self):
        queryset = PhoneNumber.objects.all()
        search_q = self.request.GET.get('q')
        
        if search_q:
            queryset = queryset.filter(tel__icontains=search_q)

        return queryset
    
    

class ExportVCardView(View):
    def get(self, request, *args, **kwargs):
        contacts = PhoneNumber.objects.all()

        vcf_data = ""
        for contact in contacts:
            vcf_data += "BEGIN:VCARD\n"
            vcf_data += "VERSION:3.0\n"
            vcf_data += f"FN:{contact.tel}\n"
            vcf_data += f"TEL;CELL:{contact.tel}\n"
            vcf_data += "END:VCARD\n"
            vcf_data += f"FN:{contact.id or contact.tel}\n"

        response = HttpResponse(vcf_data, content_type="text/vcard")
        response["Content-Disposition"] = 'attachment; filename="contacts.vcf"'

        return response
