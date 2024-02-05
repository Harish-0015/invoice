
# Test cases for invoiceDetails

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from models import invoiceDetails,invoice


class InvoiceDetailsAPITestCase(TestCase):
    def setUp(self):
        self.invoice = invoice.objects.create(date='2023-01-01', customerName='Customer 1')
        self.invoice_details = invoiceDetails.objects.create(
            invoice_id=self.invoice,
            description='Product 1',
            quantity=2,
            unitPrice=50,
            price=100
        )

    def test_get_invoice_details_list(self):
        url = reverse('invoicedetails-list')  # Assuming you've named your API view
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Product 1')

    def test_create_invoice_details(self):
        url = reverse('invoicedetails-list')
        data = {'invoice_id': self.invoice.id, 'description': 'Product 2', 'quantity': 1, 'unitPrice': 30, 'price': 30}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(invoiceDetails.objects.count(), 2)
