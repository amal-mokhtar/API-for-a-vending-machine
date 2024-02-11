# views.py
from rest_framework import viewsets
from .models import Product, VendingUser
from .serializers import ProductSerializer, VendingUserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class VendingUserViewSet(viewsets.ModelViewSet):
    queryset = VendingUser.objects.all()
    serializer_class = VendingUserSerializer

    def create(self, request, *args, **kwargs):
        # Allow creating users without authentication for simplicity
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

