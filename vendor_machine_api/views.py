from rest_framework import generics, permissions, status
from .permissions import *
from rest_framework.response import Response
from .models import User, Buyer, Seller, Product
from .serializers import UserSerializer, BuyerSerializer, SellerSerializer, ProductSerializer

class listUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  


class createBuyer(generics.CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [IsBuyerOrSeller]   

class createSeller(generics.CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsBuyerOrSeller]   


class UserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdminPermission]

class BuyerRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [IsOwnerOrAdminPermission]

class SellerRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsOwnerOrAdminPermission]









