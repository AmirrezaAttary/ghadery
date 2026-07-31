from django.urls import path
from . import views

app_name = 'paziresh'

urlpatterns = [
    path('list/', views.PazireshListView.as_view(), name='paziresh-list'),
    path('create/', views.PazireshCreateView.as_view(), name='paziresh-create'),
    path('update/<int:pk>/', views.PazireshUpdateView.as_view(), name='paziresh-update'),
    path('faktor/<int:pk>/', views.PazireshFaktorDetail.as_view(), name='paziresh-faktor'),
    path('inquiry/', views.PazireshInquiryView.as_view(), name='paziresh-inquiry'),
]

urlpatterns += [
    path('warranty/list/', views.WarrantyListView.as_view(), name='warranty-list'),
    path('warranty/create/', views.WarrantyCreateView.as_view(), name='warranty-create'),
    path('warranty/update/<int:pk>/', views.WarrantyUpdateView.as_view(), name='warranty-update'),
    path('warranty/print/<int:pk>/', views.WarrantyPrintDetail.as_view(), name='warranty-print'),
]