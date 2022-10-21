from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views
from .views import MusicViewSet, AlbumViewSet

router = DefaultRouter()
router.register('album', AlbumViewSet)
router.register('music', MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]
