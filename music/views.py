from django.shortcuts import render
from rest_framework import viewsets, generics

from music.models import Music
from music.serializers import MusicSerializer


class MusicViewSet(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer
#
#
# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer
#
#
# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer
