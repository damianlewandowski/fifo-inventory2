from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
import logging


class InventoryValueTestCase(APITestCase):
    def setUp(self):
        self.endpoint = reverse('inventory_value')

        # insert some bought items
        self.bought_endpoint = reverse('bought-list')
        bought_item1 = {'date': '2020-03-08', 'quantity': 10, 'cost_per_item': 1.0}
        bought_item2 = {'date': '2020-03-09', 'quantity': 5, 'cost_per_item': 2.0}
        bought_item3 = {'date': '2020-03-10', 'quantity': 20, 'cost_per_item': 3.0}
        bought_items = [bought_item1, bought_item2, bought_item3]

        for item in bought_items:
            self.client.post(self.bought_endpoint, item)

        #insert some sold items
        self.sold_endpoint = reverse('sold-list')
        sold_item1 = {'date': '2020-03-09', 'quantity': 12}
        sold_item2 = {'date': '2020-03-12', 'quantity': 5}
        sold_item3 = {'date': '2020-03-15', 'quantity': 3}
        sold_items = [sold_item1, sold_item2, sold_item3]

        for item in sold_items:
            self.client.post(self.sold_endpoint, item)

        self.bought_items_total_value = sum([item['quantity'] * item['cost_per_item'] for item in bought_items])
        self.bought_items_total_count = sum([item['quantity'] for item in bought_items])

        self.sold_items_total_count = sum([item['quantity'] for item in sold_items])

    def test_inventory_value_date_extreme_start(self):
        year = 2020
        month = 3
        day = 9

        response = self.client.get(self.endpoint, {'year': year, 'month': month, 'day': day})
        expected_value = 6.0
        received_value = response.data['inventory_value']

        self.assertEqual(expected_value, received_value)

    def test_inventory_value_date_extreme_end(self):
        year = 2020
        month = 3
        day = 15

        response = self.client.get(self.endpoint, {'year': year, 'month': month, 'day': day})
        expected_value = 45.0
        received_value = response.data['inventory_value']

        self.assertEqual(expected_value, received_value)


    def test_inventory_value_date_between(self):
        year = 2020
        month = 3
        day = 13

        response = self.client.get(self.endpoint, {'year': year, 'month': month, 'day': day})
        expected_value = 54.0
        received_value = response.data['inventory_value']

        self.assertEqual(expected_value, received_value)