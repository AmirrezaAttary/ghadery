from django.contrib import admin
from .models import DeviceReception


@admin.register(DeviceReception)
class DeviceReceptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "device_name",
        "device_type",
        "device_model",
        "owner_name",
        "owner_phone",
        "entry_date",
        "exit_date",
        "is_ready",
        "has_warranty",
        "created_by",
    )
    list_filter = (
        "device_type",
        "has_warranty",
        "is_ready",
        "entry_date",
        "exit_date",
    )
    search_fields = (
        "device_name",
        "device_model",
        "device_serial",
        "owner_name",
        "owner_phone",
        "owner_national_id",
        "created_by__phone_number",
    )
    readonly_fields = ("entry_date",)
    autocomplete_fields = ("created_by",)
    ordering = ("-id",)
    date_hierarchy = "entry_date"
