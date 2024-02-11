
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    # use the built-in User Model in Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    deposit = models.IntegerField(default=0)
    role = models.CharField(max_length=10, choices=[('seller', 'Seller'), ('buyer', 'Buyer')])

class Product(models.Model):
    # amoutAvailable refers to Quantity (?)
    amountAvailable = models.PositiveIntegerField()
    cost = models.PositiveSmallIntegerField()
    productName = models.CharField(max_length=32)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)







