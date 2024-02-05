
# Test cases for invoice

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from models import invoice

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.invoice = invoice.objects.create(date='2023-01-01', customerName='Customer 1')

    def test_get_invoice_list(self):
        url = reverse('invoice-list')  # Assuming you've named your API view
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Customer 1')

    def test_create_invoice(self):
        url = reverse('invoice-list')
        data = {'date': '2023-01-01', 'customerName': 'New Customer'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(invoice.objects.count(), 2)

