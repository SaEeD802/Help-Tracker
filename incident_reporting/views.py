from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.http import JsonResponse
from .models import IncidentReport
from django.conf import settings


# Create your views here.
# خانه
def index(request):
    reports = IncidentReport.objects.filter(is_verified=True)
    return render(request, 'incident_reporting/index.html', {'reports': reports})


# داده های حادثه
def incident_data(request):
    reports = IncidentReport.objects.filter(is_verified=True).values('description', 'location_lat', 'location_long', 'image', 'timestamp')
    data = list(reports)
    for item in data:
        if item['image']:
            item['image'] = request.build_absolute_uri(settings.MEDIA_URL + item['image'])
    return JsonResponse(data, safe=False)


# گزارش حادثه
def report_incident(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        location_lat = request.POST.get('location_lat')
        location_long = request.POST.get('location_long')
        image = request.FILES.get('image')

        report = IncidentReport(
            description=description,
            location_lat=location_lat,
            location_long=location_long,
            image=image
        )
        report.save()
        # return JsonResponse({'success': True})
        return redirect('index')
    return render(request, 'incident_reporting/report.html')


# مدیریت گزارش ها
@login_required
def manage_reports(request):
    reports = IncidentReport.objects.all()
    return render(request, 'incident_reporting/manage_reports.html', {'reports': reports})


# تأیید گزارش
@login_required
def verify_report(request, report_id):
    report = get_object_or_404(IncidentReport, id=report_id)
    report.is_verified = True
    report.save()
    return redirect('manage_reports')