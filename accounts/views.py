from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from products.serializers import ProductSerializer
from .models import Buyer
from products.models import Product
from .serializers import UserSerializer, BuyerSerializer, SellerSerializer

################## LOGIN and SIGNUP ##################
class BuyerSignUp(generics.CreateAPIView):
    serializer_class = BuyerSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user_data = response.data
        return Response({"message": "User created successfully!", "user_data": user_data}, status=response.status_code)

class SellerSignUp(generics.CreateAPIView):
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user_data = response.data
        return Response({"message": "User created successfully!", "user_data": user_data}, status=response.status_code)

class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "User logged out successfully!"}, status=status.HTTP_200_OK)
    


################## Seller and Buyer Funtionalities ##################
class Deposit(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            if user.role != 'buyer':
                raise permissions.PermissionDenied("You are not authorized to make deposits.")

            amount = request.data.get('amount')
            if amount not in [5, 10, 20, 50, 100]:
                raise ValueError("Invalid deposit amount.")

            buyer = Buyer.objects.get(id=user.id)
            buyer.deposit += amount
            buyer.save()

            return Response({"message": "Deposit successful!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class Buy(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            if user.role != 'buyer':
                raise permissions.PermissionDenied("You are not authorized to make purchases.")

            product_id = request.data.get('productId')
            amount = request.data.get('amount')

            product = Product.objects.get(id=product_id)
            if amount > product.amountAvailable:
                raise ValueError("Insufficient quantity available.")

            total_cost = product.cost * amount

            buyer = Buyer.objects.get(id=user.id)
            if buyer.deposit < total_cost:
                raise ValueError("Insufficient funds in your account.")

            buyer.deposit -= total_cost
            buyer.save()

            product.amountAvailable -= amount
            product.save()

            serializer = ProductSerializer(product)

            return Response({"message": "Purchase successful!", "total_spent": total_cost, "products_purchased": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class ResetDeposit(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            if user.role != 'buyer':
                raise permissions.PermissionDenied("You are not authorized to reset your deposit.")

            buyer = Buyer.objects.get(id=user.id)
            buyer.deposit = 0
            buyer.save()

            return Response({"message": "Deposit reset successful!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)