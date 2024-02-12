from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Product

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'amountAvailable', 'cost', 'productName', 'sellerId']

# class VendingUserSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = VendingUser
#         fields = ['id', 'user', 'deposit', 'role']
