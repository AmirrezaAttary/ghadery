from django.db.models.signals import post_save
from django.dispatch import receiver
from app.paziresh.models import DeviceReception
from app.website.models import PhoneNumber


@receiver(post_save, sender=DeviceReception)
def create_phone_number(sender, instance, created, **kwargs):
    if created and instance.owner_phone:
        PhoneNumber.objects.get_or_create(
            tel=instance.owner_phone
        )
