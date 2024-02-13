from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('buyer/signup/', BuyerSignUp.as_view(), name='buyer-create'),
    path('seller/signup/', SellerSignUp.as_view(), name='seller-create'),
    path('login/', Login.as_view(), name='login'),
    # path('logout/', Logout.as_view(), name='logout'),


    path('users/', listUsers.as_view(), name='user-list'),

]
