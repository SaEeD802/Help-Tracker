from django.contrib import admin
from .models import IncidentReport


# Register your models here.
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('description', 'timestamp', 'is_verified')


admin.site.register(IncidentReport, IncidentReportAdmin)
