from django.shortcuts import render
from rest_framework import viewsets, permissions
from category.models import Category
from . import serializers
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return serializers.Category
#         return serializers.CategoryDetailSerializer
#
#     def get_permissions(self):
#
#         if self.action == 'list':
#             permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#         else:
#             permissions_classes = (permissions.IsAdminUser,)
#         return [permission() for permission in permission_classes]



