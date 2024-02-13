from rest_framework import generics, permissions, status


class IsBuyerOrSeller(permissions.BasePermission):
    def hasPermission(self, request, view):
        return request.user.is_authenticated or request.data.get('role') in ['BUYER', 'SELLER']

class IsOwnerOrAdminPermission(permissions.BasePermission):
    def hasPermission(self, request, view, obj):
        return obj == request.user or request.user.role == 'ADMIN'