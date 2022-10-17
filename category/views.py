from django.shortcuts import render
from rest_framework import viewsets
from serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategorySerializer
    serializer_class = CategorySerializer
