from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class BoughtViewSetTestCase(APITestCase):
    def setUp(self):
        self.endpoint = reverse('bought-list')

    def test_succesful_add_new_bought(self):
        item = {'date': '2020-03-10', 'quantity': 10, 'cost_per_item': 5}
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, 201)

    def test_should_fail_add_new_bought(self):
        # quantity can't be a string
        item = {'date': '2020-03-10', 'quantity': 'dasdas', 'cost_per_item': 5}
        response = self.client.post(self.endpoint, item)
        self.assertEqual(response.status_code, 400)