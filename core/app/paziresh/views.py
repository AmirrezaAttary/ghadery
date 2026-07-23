from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import DeviceReception
from .forms import DeviceReceptionForm,DeviceUpdateReceptionForm
# Create your views here.
from django.http import JsonResponse
from django.views import View



class PazireshListView(LoginRequiredMixin,ListView):
    template_name = "paziresh/list.html"
    model = DeviceReception
    paginate_by = 20
    def get_queryset(self):
        queryset = DeviceReception.objects.all()
        search_q = self.request.GET.get('q')

        if search_q:
            queryset = queryset.filter(
                Q(id__icontains=search_q) |
                Q(device_name__icontains=search_q) |
                Q(owner_name__icontains=search_q) |
                Q(owner_phone__icontains=search_q) |
                Q(owner_national_id__icontains=search_q)
            )
        if self.request.GET.get('is_ready') in ['true', 'false']:
            is_ready = self.request.GET.get('is_ready') == 'true'
            queryset =queryset.filter(is_ready=is_ready)
        return queryset
    
    
class PazireshCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = "paziresh/create.html"
    model = DeviceReception
    form_class = DeviceReceptionForm
    success_url = "/paziresh/list/"
    success_message = "دستگاه با موفقیت پذیریش شد."
    
    
class PazireshUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    template_name = "paziresh/update.html"
    model = DeviceReception
    form_class = DeviceUpdateReceptionForm
    success_url = "/paziresh/list/"
    success_message = "دستگاه با موفقیت ویرایش شد."
    
class PazireshFaktorDetail(DetailView):
    template_name = "paziresh/faktor.html"
    model = DeviceReception
    

class PazireshInquiryView(LoginRequiredMixin, View):
    def get(self, request):
        national_id = request.GET.get('national_id', '').strip()

        if not national_id:
            return JsonResponse({'found': False, 'message': 'کد ملی وارد نشده است.'})

        reception = (
            DeviceReception.objects
            .filter(owner_national_id=national_id)
            .order_by('-id')
            .first()
        )

        if not reception:
            return JsonResponse({'found': False, 'message': 'سابقه‌ای برای این کد ملی یافت نشد.'})

        data = {
            'owner_name': reception.owner_name,
            'owner_phone': reception.owner_phone,
            'owner_landline': reception.owner_landline or '',
            'owner_address': reception.owner_address,
        }
        return JsonResponse({'found': True, 'data': data})