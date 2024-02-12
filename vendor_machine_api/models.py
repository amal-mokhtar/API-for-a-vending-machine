
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

    # use the built-in User Model in Django


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
    # deposit = models.PositiveIntegerField(default=0)
    buyer = BuyerManager()
    class Meta:
        proxy = True

    def hi(self):
        return "hello"
        

class SellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SELLER)


class Seller(User):

    baseRole = User.Role.SELLER

    seller = SellerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for sellers"
    


    # def deposit(self, amount):
    #         if self.role == 'buyer':
    #             self.deposit += amount
    #             self.save()
    #         else:
    #             raise PermissionError("You're not authorized to deposit coins")


        

class Product(models.Model):
    # amoutAvailable refers to Quantity (?)
    amountAvailable = models.PositiveIntegerField()
    cost = models.PositiveSmallIntegerField()
    productName = models.CharField(max_length=32)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName


            













