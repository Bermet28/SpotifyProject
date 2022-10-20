from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, permissions, response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from comments_likes.models import Like, Favorites
from comments_likes.serializers import CommentSerializer, LikeSerializer
from . import serializers
from account import permissions as per
from music.models import Music, Album
from music.serializers import MusicSerializer, AlbumSerializer


class StandartResultPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 1000


class MusicView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category',)
    seacrh_fields = ('name',)
    pagination_class = StandartResultPagination
    serializer_class = MusicSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return serializers.MusicListSerializer
    #     return serializers.MusicDetailSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer




    # def get_permissions(self):
    #     #создавать может только залогиненный юзер
    #     if self.action in ('create', 'add_to_liked', 'remove_from_liked', 'get_likes',):
    #         return [permissions.IsAuthenticated()]
    #     #изменять и удалять может только исполнитель
    #     elif self.action in ('update', 'partial_update', 'destroy',):
    #         return [per.IsAccountOwner()]
    #     #Просматривать могут все
    #     else:
    #         return [permissions.AllowAny()]
    #
    #     # @action(['GET', 'POST'], detail=True)
    #     # def reviews(self, request, pk=None):
    #     #     music = self.get_object()
    #     #     if request.method == 'GET':
    #     #         reviews = music.reviews.all()
    #     #         serializer = ReviewSerializer(data=data, context={'request': request, 'music': music})
    #     #         serializer.is_valid(raise_exception=True)
    #     #         serializer.save()
    #     #         return response.Response(serializer.data, status=201)
    # @action(['GET'], detail=True,)
    # def comments(self, request, pk):
    #     music = self.get_object()
    #     comments = music.comments.all()
    #     serializer = CommentSerializer(comments, many=True)
    #     return response.Response(serializer.data, status=200)
    #
    # @action(['POST'], detail=True,)
    # def add_to_liked(self, request, pk):
    #     music = self.get_object()
    #     if request.user.liked.filter(music=music).exists():
    #         return response.Response("Вы уже поставили лайк", status=400)
    #     Like.objects.create(music=music, owner=request.user)
    #     return response.Response('Вы поставили лайк', status=201)
    #
    # @action(['POST'], detail=True,)
    # def remove_from_liked(self, request, pk):
    #     music = self.get_object()
    #     if request.user.liked.filter(music=music).exists():
    #         return response.Response("Вы не лайклаи этот пост", status=400)
    #     request.user.liked.filter(music=music).delete()
    #     return response.Response("Ваш лайк удален", status=204)
    #
    # @action(['GET'], detail=True,)
    # def get_likes(self, request):
    #     music = self.get_object()
    #     likes = music.likes.all()
    #     serializer = LikeSerializer(likes, many=True)
    #     return response.Response(serializer.data, status=200)
    # @action(['POST'], detail=True)
    # def favorite(self, request, pk):
    #     music = self.get_object()
    #     if request.user.favorites.filter(music=music).exists():
    #         request.user.favorites.filter(music=music).delete()
    #         return response.Response("Убрано из избранных", status=204)
    #     Favorites.objects.create(music=music, owner=request.user)
    #     return response.Response("Добавлено в избранные", status=201)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

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
