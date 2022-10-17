from django.db import models
from account import Customuser
from category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


class Music(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='music')
    image = models.ImageField(upload_to='images')
    track = models.FileField(upload_to='mp3')



