from django.db import models

# Create your models here.
class productModel(models.Model):
    productName =models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()