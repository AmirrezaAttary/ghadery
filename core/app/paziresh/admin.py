from django.contrib import admin

from .models import DeviceReception, Warranty


# =========================================================
# Device Reception Admin
# =========================================================

@admin.register(DeviceReception)
class DeviceReceptionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "device_name",
        "device_type",
        "device_model",
        "owner_name",
        "owner_phone",
        "status",
        "has_warranty",
        "reception_type",
        "delivery_type",
        "entry_date",
        "exit_date",
        "created_by",
    )

    list_filter = (
        "status",
        "device_type",
        "has_warranty",
        "reception_type",
        "delivery_type",
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

    readonly_fields = (
        "entry_date",
    )

    autocomplete_fields = (
        "created_by",
    )

    ordering = (
        "-id",
    )

    date_hierarchy = "entry_date"

    fieldsets = (
        (
            "اطلاعات پذیرش",
            {
                "fields": (
                    "entry_date",
                    "exit_date",
                    "status",
                    "created_by",
                )
            },
        ),

        (
            "مشخصات دستگاه",
            {
                "fields": (
                    "device_name",
                    "device_type",
                    "device_model",
                    "device_serial",
                )
            },
        ),

        (
            "مشخصات مالک",
            {
                "fields": (
                    "owner_name",
                    "owner_phone",
                    "owner_national_id",
                    "owner_landline",
                    "owner_address",
                )
            },
        ),

        (
            "اطلاعات تعمیر",
            {
                "fields": (
                    "appearance_issue",
                    "description",
                    "technician_note",
                    "cost",
                )
            },
        ),

        (
            "گارانتی",
            {
                "fields": (
                    "has_warranty",
                    "warranty_period",
                )
            },
        ),

        (
            "نوع پذیرش و تحویل",
            {
                "fields": (
                    "reception_type",
                    "delivery_type",
                )
            },
        ),
    )


# =========================================================
# Warranty Admin
# =========================================================

@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "device",
        "start_date",
        "end_date",
        "is_active",
        "issued_by",
        "created_at",
    )

    list_filter = (
        "start_date",
        "end_date",
        "created_at",
    )

    search_fields = (
        "device__owner_name",
        "device__device_name",
        "device__device_model",
        "device__device_serial",
        "device__owner_national_id",
        "device__owner_phone",
    )

    autocomplete_fields = (
        "device",
        "issued_by",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-id",
    )

