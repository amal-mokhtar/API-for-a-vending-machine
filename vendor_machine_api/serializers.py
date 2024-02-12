from rest_framework import serializers
from .models import User, Buyer, Seller, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'deposit']

class BuyerSerializer(UserSerializer):
    class Meta:
        model = Buyer
        fields = UserSerializer.Meta.fields + []

class SellerSerializer(UserSerializer):
    class Meta:
        model = Seller
        fields = UserSerializer.Meta.fields + []

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'amountAvailable', 'cost', 'productName', 'seller']