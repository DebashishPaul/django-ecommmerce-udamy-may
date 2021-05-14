from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=255)
    current_price = models.FloatField()
    real_price = models.FloatField()
    image = models.CharField(max_length=500)


class Order(models.Model):
    
    item = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total = models.FloatField()
    def __str__(self):
        return self.name