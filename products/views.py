from rest_framework import generics, permissions, status
from .models import Product
from .serializers import ProductSerializer

class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, serializer):
        seller = self.request.user
        serializer.save(seller=seller)

    def update(self, serializer):
        product = self.get_object()
        if product.seller != self.request.user:
            raise permissions.PermissionDenied("You are not authorized to update this product.")
        serializer.save()

    def delete(self, instance):
        if instance.seller != self.request.user:
            raise permissions.PermissionDenied("You are not authorized to delete this product.")
        instance.delete()