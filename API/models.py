from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=240)

class Products(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.IntegerField(max_length=200)
    expiry_date = models.DateField()