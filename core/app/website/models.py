from django.db import models
from app.accounts.validators import validate_iranian_cellphone_number

# Create your models here.
class SMSNumber(models.Model):
    number = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-id']

class PhoneNumber(models.Model):
    tel = models.CharField(max_length=12,unique=True, validators=[validate_iranian_cellphone_number],null=True,blank=True)
    
    class Meta:
        ordering = ['-id']