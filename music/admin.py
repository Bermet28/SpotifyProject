from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Music, Album, Like


# from .views import MusicView
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.urls} width="50" height = "60"')

    get_image.short_description = 'Poster'


admin.site.register(Music, MusicAdmin),
admin.site.register(Album),
admin.site.register(Like)
