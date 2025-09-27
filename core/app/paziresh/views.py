from django.views.generic import ListView,CreateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import DeviceReception
from .forms import DeviceReceptionForm,DeviceUpdateReceptionForm
# Create your views here.


class PazireshListView(ListView):
    template_name = "paziresh/list.html"
    model = DeviceReception
    paginate_by = 10
    
    
class PazireshCreateView(SuccessMessageMixin,CreateView):
    template_name = "paziresh/create.html"
    model = DeviceReception
    form_class = DeviceReceptionForm
    success_url = "/paziresh/list/"
    success_message = "دستگاه با موفقیت پذیریش شد."
    
    
class PazireshUpdateView(SuccessMessageMixin,UpdateView):
    template_name = "paziresh/update.html"
    model = DeviceReception
    form_class = DeviceUpdateReceptionForm
    success_url = "/paziresh/list/"
    success_message = "دستگاه با موفقیت ویرایش شد."
    
    