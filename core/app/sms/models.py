from django.db import models

from app.accounts.models import User


class SMSLog(models.Model):

    STATUS_CHOICES = [
        ("pending", "در انتظار"),
        ("success", "موفق"),
        ("failed", "ناموفق"),
    ]

    SEND_TYPES = [
        ("single", "ارسال تکی"),
        ("ready_device", "آماده تحویل"),
        ("bulk", "ارسال گروهی"),
    ]

    receptor = models.CharField(
        max_length=20,
        verbose_name="شماره گیرنده"
    )

    sender = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="شماره ارسال کننده"
    )

    message = models.TextField(
        verbose_name="متن پیام"
    )

    send_type = models.CharField(
        max_length=30,
        choices=SEND_TYPES,
        default="single",
        verbose_name="نوع ارسال"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name="وضعیت"
    )

    message_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="شناسه پیام کاوه نگار"
    )

    error_message = models.TextField(
        blank=True,
        null=True,
        verbose_name="خطا"
    )

    sent_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sms_logs",
        verbose_name="ارسال توسط"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ارسال"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "گزارش پیامک"
        verbose_name_plural = "گزارش پیامک‌ها"

    def __str__(self):
        return f"{self.receptor} - {self.get_status_display()}"

