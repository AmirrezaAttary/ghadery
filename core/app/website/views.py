from django.views.generic import TemplateView,CreateView,ListView

# Create your views here.

class HomeView(TemplateView):
    template_name = "website/home.html"