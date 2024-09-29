from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_jalali.db import models as jmodels


# Create your models here.
# گزارش حادثه
class IncidentReport(models.Model):
    """
    مدل برای ذخیره گزارشات حوادث شامل توضیحات، مکان جغرافیایی، تصویر و وضعیت تایید
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='کاربر')
    description = models.TextField(verbose_name='جزئیات')
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='عرض جغرافیایی')
    location_long = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='طول جغرافیایی')
    image = models.ImageField(upload_to='incident_images/', null=True, blank=True, verbose_name='تصویر حادثه')
    timestamp = jmodels.jDateTimeField(default=timezone.now, verbose_name='زمان ثبت')
    is_verified = models.BooleanField(default=False, verbose_name='تایید شده')

    class Meta:
        verbose_name = 'گزارش حوادث'
        verbose_name_plural = 'گزارش حوادث'

    def __str__(self):
        return f"{self.description[:50]} - {self.timestamp.strftime('%Y-%m-%d')}"
