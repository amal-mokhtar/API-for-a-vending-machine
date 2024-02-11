
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


            


    # def make_purchase(self, product_price):
    #     if self.role == 'buyer' and self.deposit >= product_price:
    #         self.deposit -= product_price
    #         self.save()
    #         return True
    #     elif self.role == 'buyer':
    #         raise PermissionError("Insufficient funds for the purchase")
    #     else:
    #         raise PermissionError("You're not authorized to make purchases")

    # def add_product(self, product_name, product_price):
    #     if self.role == 'seller':
    #         Product.objects.create(name=product_name, price=product_price, seller_id=self.id)
    #         return True
    #     else:
    #         raise PermissionError("You're not authorized to add products")

    # def update_product(self, product_id, new_price):
    #     if self.role == 'seller':
    #         try:
    #             product = Product.objects.get(id=product_id, seller_id=self.id)
    #             product.price = new_price
    #             product.save()
    #             return True
    #         except Product.DoesNotExist:
    #             raise PermissionError("Product not found or you're not authorized to update it")
    #     else:
    #         raise PermissionError("You're not authorized to update products")

    # def remove_product(self, product_id):
    #     if self.role == 'seller':
    #         try:
    #             product = Product.objects.get(id=product_id, seller_id=self.id)
    #             product.delete()
    #             return True
    #         except Product.DoesNotExist:
    #             raise PermissionError("Product not found or you're not authorized to remove it")
    #     else:
    #         raise PermissionError("You're not authorized to remove products")










