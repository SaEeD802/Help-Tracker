from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report_incident, name='report_incident'),
    path('manage/', views.manage_reports, name='manage_reports'),
    path('verify/<int:report_id>/', views.verify_report, name='verify_report'),
    path('incident-data/', views.incident_data, name='incident_data'),
]
