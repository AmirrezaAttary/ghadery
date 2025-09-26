from django.views.generic import ListView,CreateView
from .models import DeviceReception
from .forms import DeviceReceptionForm
# Create your views here.


class PazireshListView(ListView):
    template_name = "paziresh/list.html"
    model = DeviceReception
    paginate_by = 10
    
    
class PazireshDetailView(CreateView):
    template_name = "paziresh/create.html"
    model = DeviceReception
    form_class = DeviceReceptionForm
    success_url = "/paziresh/list/"