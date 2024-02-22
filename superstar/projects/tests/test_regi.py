from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from projects.views import project_details

class TestRegi(SimpleTestCase):

    def test_emriFunksionit(self):
        response = self.client.get(reverse('project_details', args=[19]))
        self.assertEqual(response.status_code, 302)