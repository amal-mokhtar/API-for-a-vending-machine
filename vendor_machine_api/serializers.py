from rest_framework import serializers
from .models import User, Buyer, Seller, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
        read_only_fields = ['role'] 

class BuyerSerializer(UserSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'username', 'password', 'role', 'deposit']
        read_only_fields = ['role'] 

class SellerSerializer(UserSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'username',  'password', 'role']
        read_only_fields = ['role'] 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'amountAvailable', 'cost', 'productName', 'seller']
        read_only_fields = ['seller'] 