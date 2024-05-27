from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=240)

class Products(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField()
    stock = models.IntegerField()
    expiry_date = models.DateTimeField()