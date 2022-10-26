from django.db import models
from mutagen.mp3 import MP3
from category.models import Category
from django.contrib.auth import get_user_model
from music.helpers import get_audio_length
from music.validators import validate_is_audio

User = get_user_model()


class Music(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='music')
    image = models.ImageField(upload_to='images')
    track = models.FileField(upload_to='mp3', validators=[validate_is_audio])
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music', null=True)
    # album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    time_length = models.DecimalField(blank=True, max_digits=20, decimal_places=2, null=True)

    # def get_audio_length(file):
    #     audio = MP3(file)
    #     return audio.info.length

    def save(self, *args, **kwargs):
        if not self.time_length:
            # logic for getting music length here
            audio_length = get_audio_length(self.track)
            self.time_length = audio_length
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} --------------->   {self.image}'


class Album(models.Model):
    name = models.CharField(max_length=150)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ->{self.music}'


class Like(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='likes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['music', 'owner']

    def __str__(self):
        return f'{self.music} -> {self.owner}'
