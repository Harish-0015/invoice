from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


# Create your models here.
class invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100)
    customerName = models.CharField(max_length=20)

    class Meta:
        app_label = 'invoiceApp'
        db_table = 'invoice'

class invoiceDetails(models.Model):
    invoice_id=models.ForeignKey(invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    unitPrice = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    class Meta:
        app_label = 'invoiceApp'
        db_table = "invoiceDetail"

