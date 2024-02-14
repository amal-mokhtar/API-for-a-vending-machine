from rest_framework import serializers
from .models import User, Buyer, Seller

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'role']
        read_only_fields = ['role'] 

class BuyerSerializer(UserSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'username', 'role', 'deposit']
        read_only_fields = ['role'] 

class SellerSerializer(UserSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'username', 'role']
        read_only_fields = ['role'] 