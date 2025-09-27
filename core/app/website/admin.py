from django.contrib import admin
from .models import SMSNumber,PhoneNumber

# Register your models here.

@admin.register(SMSNumber)
class SMSAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)
    
    
@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('tel',)
    search_fields = ('tel',)