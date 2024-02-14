from django.contrib import admin
from .models import User, Buyer, Seller

admin.site.register(User)

class BuyerAdmin(admin.ModelAdmin):
    exclude = 'role',

    def has_change_permission(self, *args, **kwargs):
        return False

admin.site.register(Buyer, BuyerAdmin)

class SellerAdmin(admin.ModelAdmin):
    ...

admin.site.register(Seller, SellerAdmin)