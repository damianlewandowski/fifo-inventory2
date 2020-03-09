from django.test import TestCase

# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


class SoldViewSetTestCase(APITestCase):
    def setUp(self):
        self.endpoint = reverse('sold-list')

    def test_succesful_add_new_sold(self):
        item = {'date': '2020-03-10', 'quantity': 10}
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, 201)

    def test_should_fail_add_new_sold(self):
        # quantity can't be a string
        item = {'date': '2020-03-10', 'quantity': 'dasdas'}
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, 400)