# # views.py
# from rest_framework import viewsets
# from .models import Product, VendingUser
# from .serializers import ProductSerializer, VendingUserSerializer


# get all products
# serialize them
# return json


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

