from django.urls import path
from . import views

app_name = 'paziresh'

urlpatterns = [
    path('list/', views.PazireshListView.as_view(), name='paziresh-list'),
    path('create/', views.PazireshDetailView.as_view(), name='paziresh-create'),
]
