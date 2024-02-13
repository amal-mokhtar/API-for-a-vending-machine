from rest_framework import serializers
from .models import User, Buyer, Seller, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'passsword', 'role']

class BuyerSerializer(UserSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'username', 'role',  'passsword', 'deposit']

class SellerSerializer(UserSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'username',  'passsword', 'role', ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'amountAvailable', 'cost', 'productName', 'sellerId']