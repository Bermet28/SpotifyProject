from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views
from .views import MusicView, AlbumViewSet

router = DefaultRouter()
router.register('album', AlbumViewSet)

urlpatterns = [
    path('music/', views.MusicView.as_view()),
    path('', include(router.urls)),
]
