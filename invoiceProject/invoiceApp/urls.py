# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('invoice/', invoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoice/<int:pk>/', invoiceUpdateView.as_view(), name='invoice-update'),
    path('invoiceDetails/', invoiceDetailsListCreateView.as_view(), name='invoiceDetails-list-create'),
    path('invoiceDetails/<int:pk>/', invoiceDetailsUpdateView.as_view(), name='invoiceDetails-update'),
    
    
]