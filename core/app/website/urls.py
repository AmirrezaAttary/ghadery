from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('smsnumbers/', views.SMSNumberListView.as_view(), name='smsnumber_list'),
    path('smsnumbers/add/', views.SMSNumberCreateView.as_view(), name='smsnumber_add'),
    path('phonenumbers/', views.PhoneNumberListView.as_view(), name='phonenumber_list'),
    path('phonenumbers/add/', views.PhoneNumberCreateView.as_view(), name='phonenumber_add'),
]
