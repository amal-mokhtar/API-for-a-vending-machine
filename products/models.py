from django.db import models
from accounts.models import Seller

class Product(models.Model):
    # amoutAvailable refers to Quantity (?)
    amountAvailable = models.PositiveIntegerField()
    cost = models.PositiveSmallIntegerField()
    productName = models.CharField(max_length=32)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName