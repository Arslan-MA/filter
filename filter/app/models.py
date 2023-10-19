from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    seller = models.CharField(max_length=255)
    stock_quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    application_area = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name
