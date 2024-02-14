from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'amountAvailable', 'cost', 'productName', 'seller']
        read_only_fields = ['seller']