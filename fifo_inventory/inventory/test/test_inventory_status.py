from django.test import TestCase

# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class InventoryStatusTestCase(APITestCase):
    def setUp(self):
        self.endpoint = reverse('inventory_status')

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

    def test_inventory_status_date_in_range_of_items(self):
        year = 2020
        month = 3
        day = 10
        response = self.client.get(self.endpoint, {'year': year, 'month': month, 'day': day})
        received_quantity = response.data['quantity']
        expected_quantity = 23
        self.assertEqual(received_quantity, expected_quantity)

    def test_inventory_status_no_sold_in_date_ultimo(self):
        year = 2020
        month = 3
        day = 8
        response = self.client.get(self.endpoint, {'year': year, 'month': month, 'day': day})
        received_quantity = response.data['quantity']
        expected_quantity = 10
        self.assertEqual(received_quantity, expected_quantity)

    # The result should be total bought - total sold
    def test_inventory_status_sold_date_at_the_end(self):
        year = 2020
        month = 3
        day = 15
        response = self.client.get(self.endpoint, {'year': year, 'month': month, 'day': day})
        received_quantity = response.data['quantity']
        expected_quantity = self.bought_items_total_count - self.sold_items_total_count
        self.assertEqual(received_quantity, expected_quantity)

    # The result should be 0 since nothing was bought or sold ultimo day 1
    def test_inventory_status_no_bought_or_sold(self):
        year = 2020
        month = 3
        day = 1
        response = self.client.get(self.endpoint, {'year': year, 'month': month, 'day': day})
        received_quantity = response.data['quantity']
        expected_quantity = 0
        self.assertEqual(received_quantity, expected_quantity)