from django.db import models
from django.contrib.auth.models import AbstractUser

# multi-table inheritance. 
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=[('seller', 'Seller'), ('buyer', 'Buyer')])

    class Meta:
        abstract = True


        
class Seller(User):
# explicitly setting the role for each subclass to prevent creating instances with incorrect roles.
    def save(self, *args, **kwargs):
        self.role = 'seller'
        super().save(*args, **kwargs)


class Buyer(User):
    deposit = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.role = 'buyer'
        super().save(*args, **kwargs)



class Product(models.Model):

    # amoutAvailable refers to Quantity (?)
    amountAvailable = models.PositiveIntegerField()
    cost = models.PositiveSmallIntegerField()
    productName = models.CharField(max_length=32)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)




