from django.contrib import admin

from .models import SMSLog


@admin.register(SMSLog)
class SMSLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "receptor",
        "sender",
        "send_type",
        "status",
        "message_id",
        "sent_by",
        "created_at",
    )

    list_filter = (
        "status",
        "send_type",
        "created_at",
    )

    search_fields = (
        "receptor",
        "sender",
        "message",
        "message_id",
        "error_message",
        "sent_by__phone_number",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-id",
    )

