from django.db import models
from app.accounts.models import User
from app.accounts.validators import validate_iranian_cellphone_number


class DeviceReception(models.Model):
    # ---------------- زمان پذیرش و خروج ----------------
    entry_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ پذیرش")
    exit_date = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ خروج")

    # ---------------- مشخصات دستگاه ----------------
    DEVICE_TYPES = [
        ("tv", "تلویزیون"),
        ("monitor", "مانیتور"),
        ("projector", "پروژکتور"),
        ("other", "سایر"),
    ]

    device_name = models.CharField(max_length=100, verbose_name="نام دستگاه")
    device_type = models.CharField(
        max_length=20, choices=DEVICE_TYPES, verbose_name="نوع دستگاه"
    )
    device_model = models.CharField(max_length=100, verbose_name="مدل دستگاه")
    device_serial = models.CharField(max_length=100, unique=True, verbose_name="سریال دستگاه")

    # ---------------- مشخصات مالک ----------------
    owner_name = models.CharField(max_length=100, verbose_name="نام مالک")
    owner_phone = models.CharField(
        max_length=12,
        validators=[validate_iranian_cellphone_number],
        verbose_name="شماره تلفن همراه"
    )
    owner_national_id = models.CharField(max_length=10, verbose_name="کد ملی")
    owner_landline = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="تلفن ثابت"
    )
    owner_address = models.TextField(verbose_name="آدرس")

    # ---------------- مشخصات مشکل ----------------
    appearance_issue = models.TextField(blank=True, null=True, verbose_name="ایراد ظاهری")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    technician_note = models.TextField(blank=True, null=True, verbose_name="نظر تکنسین")
    cost = models.DecimalField(
        max_digits=12, decimal_places=0, blank=True, null=True, verbose_name="هزینه"
    )

    has_warranty = models.BooleanField(default=False, verbose_name="آیا گارانتی دارد؟")
    warranty_period = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="مدت گارانتی"
    )

    is_ready = models.BooleanField(default=False, verbose_name="آیا آماده تحویل است؟")

    # ---------------- کاربر پذیرش کننده ----------------
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="receptions",
        verbose_name="پذیرش توسط"
    )

    def __str__(self):
        return f"{self.device_name} - {self.owner_name}"
    
    class Meta:
        ordering = ['-id']
