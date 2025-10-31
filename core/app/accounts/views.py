from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AuthenticationForm

# Create your views here.
class LoginView(SuccessMessageMixin,auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_message = "با موفقیت وارد شدید."
    
    
class LogoutView(SuccessMessageMixin,auth_views.LogoutView):
    success_message = "با موفقیت خارج شدید."
    pass
