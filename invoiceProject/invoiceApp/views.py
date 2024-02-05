from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.decorators import api_view


# Create your views here.

#view for invoice Model
class invoiceListCreateView(generics.ListCreateAPIView):
    queryset = invoice.objects.all()
    serializer_class = invoiceSerializer

class invoiceUpdateView(generics.RetrieveUpdateAPIView):
    queryset = invoice.objects.all()
    serializer_class = invoiceSerializer


#view for invoice Detail Model
class invoiceDetailsListCreateView(generics.ListCreateAPIView):
    queryset = invoiceDetails.objects.all()
    serializer_class = invoiceDetailsSerializer

class invoiceDetailsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = invoiceDetails.objects.all()
    serializer_class = invoiceDetailsSerializer

