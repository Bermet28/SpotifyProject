from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from . import views
from .views import MusicViewSet

urlpatterns = [
    path('music/', views.MusicViewSet.as_view()),
]
