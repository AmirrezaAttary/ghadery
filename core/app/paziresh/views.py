from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import DeviceReception
from .forms import DeviceReceptionForm,DeviceUpdateReceptionForm
# Create your views here.


class PazireshListView(LoginRequiredMixin,ListView):
    template_name = "paziresh/list.html"
    model = DeviceReception
    paginate_by = 10
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
    
    