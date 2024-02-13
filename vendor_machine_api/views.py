from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from .permissions import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import User, Buyer, Seller, Product
from .serializers import UserSerializer, BuyerSerializer, SellerSerializer, ProductSerializer
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt


class BuyerSignUp(generics.CreateAPIView):
    serializer_class = BuyerSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            
            if response.status_code == status.HTTP_201_CREATED:
                user_data = response.data
                return Response({"message": "User created successfully!", "user_data": user_data}, status=status.HTTP_201_CREATED)
            
            return response
        
        except Exception as e:
            return Response({f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class SellerSignUp(generics.CreateAPIView):
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            
            if response.status_code == status.HTTP_201_CREATED:
                user_data = response.data
                return Response({"message": "User created successfully!", "user_data": user_data}, status=status.HTTP_201_CREATED)
            
            return response
        
        except Exception as e:
            return Response({f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@csrf_exempt
class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"An error occurred": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({f"An error occurred during login: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class Logout(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         logout(request)
#         return Response({"message": "User logged out successfully!"}, status=status.HTTP_200_OK)









class listUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  
 


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









