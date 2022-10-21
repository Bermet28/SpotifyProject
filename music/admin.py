from django.contrib import admin
from .models import Music, Album, Like

# from .views import MusicView

admin.site.register(Music)
admin.site.register(Album)
admin.site.register(Like)