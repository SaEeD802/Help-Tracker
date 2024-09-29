from django.test import TestCase
from django.urls import reverse
from .models import IncidentReport
from django.contrib.auth.models import User

class IncidentDataViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.report = IncidentReport.objects.create(
            user=self.user,
            description='Test incident description',
            location_lat=35.6892,
            location_long=51.3890,
            image='incident_images/test_image.jpg',
            is_verified=True
        )

    def test_incident_data_view(self):
        response = self.client.get(reverse('incident_data'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test incident description')
        self.assertContains(response, 'http://testserver/media/incident_images/test_image.jpg')
