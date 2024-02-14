from django.contrib import admin
from django.urls import path
from accounts.views import *
from products.views import *
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('buyer/signup/', BuyerSignUp.as_view(), name='buyer-create'),
    path('seller/signup/', SellerSignUp.as_view(), name='seller-create'),
    path('login/', Login.as_view(), name='login'),
    # path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),


    # path('products/', ListProducts.as_view(), name='product-list'),
    # path('products/<int:pk>/', ProductRUD.as_view(), name='product-detail'),
    # path('deposit/', Deposit.as_view(), name='deposit'),
    # path('buy/', Buy.as_view(), name='buy'),
    # path('reset/', ResetDeposit.as_view(), name='reset'),

]
