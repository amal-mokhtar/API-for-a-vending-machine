# # serializers.py
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Product, VendingUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'amount_available', 'cost', 'product_name', 'seller']

# class VendingUserSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = VendingUser
#         fields = ['id', 'user', 'deposit', 'role']
