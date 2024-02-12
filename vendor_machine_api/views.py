from django.http import JsonResponse



# get all products
# serialize them
# return json


from rest_framework import generics, permissions
from .models import User, Buyer, Seller, Product
from .serializers import UserSerializer, BuyerSerializer, SellerSerializer, ProductSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can list users

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required for creating users

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authentication required for retrieving, updating, or deleting a user

    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name='AdminGroup').exists() and view.action in ['retrieve', 'update', 'destroy']:
            return True
        elif user.groups.filter(name='BuyerGroup').exists() and view.action == 'create':
            return True
        elif user.groups.filter(name='SellerGroup').exists() and view.action == 'create':
            return True
        return False

class BuyerCreateView(generics.CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required for creating buyers

class SellerCreateView(generics.CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required for creating sellers

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required for listing products

 # No authentication required for listing products






def make_purchase(self, product_price):
        if self.role == 'buyer' and self.deposit >= product_price:
            self.deposit -= product_price
            self.save()
            return True
        elif self.role == 'buyer':
            raise PermissionError("Insufficient funds for the purchase")
        else:
            raise PermissionError("You're not authorized to make purchases")

def add_product(self, product_name, product_price):
        if self.role == 'seller':
            Product.objects.create(name=product_name, price=product_price, seller_id=self.id)
            return True
        else:
            raise PermissionError("You're not authorized to add products")

def update_product(self, product_id, new_price):
        if self.role == 'seller':
            try:
                product = Product.objects.get(id=product_id, seller_id=self.id)
                product.price = new_price
                product.save()
                return True
            except Product.DoesNotExist:
                raise PermissionError("Product not found or you're not authorized to update it")
        else:
            raise PermissionError("You're not authorized to update products")

def remove_product(self, product_id):
        if self.role == 'seller':
            try:
                product = Product.objects.get(id=product_id, seller_id=self.id)
                product.delete()
                return True
            except Product.DoesNotExist:
                raise PermissionError("Product not found or you're not authorized to remove it")
        else:
            raise PermissionError("You're not authorized to remove products")





# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         serializer.save(seller=self.request.user)

# class VendingUserViewSet(viewsets.ModelViewSet):
#     queryset = VendingUser.objects.all()
#     serializer_class = VendingUserSerializer

#     def create(self, request, *args, **kwargs):
#         # Allow creating users without authentication for simplicity
#         return super().create(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

