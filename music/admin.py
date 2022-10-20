from django.contrib import admin
from .models import Music, Album

# from .views import MusicView

admin.site.register(Music)
admin.site.register(Album)