
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        BUYER = "BUYER", 'Buyer'
        SELLER = "SELLER", 'Seller'

    baseRole = Role.ADMIN
    role = models.CharField(max_length=10, choices=Role.choices)
    deposit = models.IntegerField(default=0)

    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.baseRole 
            return super().save(*args, **kwargs)
        

class BuyerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.BUYER)

class Buyer(User):
    baseRole = User.Role.BUYER
    buyer = BuyerManager()
    class Meta:
        proxy = True


        

class SellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SELLER)


class Seller(User):

    baseRole = User.Role.SELLER

    seller = SellerManager()

    class Meta:
        proxy = True












