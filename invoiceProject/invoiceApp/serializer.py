# serializers.py
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate,get_user_model

class invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoice
        fields = '__all__'  

class invoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoiceDetails
        fields = '__all__'