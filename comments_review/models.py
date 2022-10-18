# from django.contrib.auth import get_user_model
# from django.db import models
# from music.models import Music
#
# User = get_user_model
#
#
# class Comment(models.Model):
#     onwer = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
#     music = models.ForeignKey(Music, related_name='comments', on_delete=models.CASCADE )
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.music} -> {self.music} -> {self.created_at}'
#
#
# class Like(models.Model):
#     music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='likes')
#     owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked')
#
#     class Meta:
#         unique_together = ['music', 'owner']
#
#
# class Favorites(models.Model):
#     music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='favorites')
#     owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
#
#     class Meta:
#         unique_together = ['music', 'owner']
#


