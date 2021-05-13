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