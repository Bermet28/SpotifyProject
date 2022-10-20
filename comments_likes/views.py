from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, response, permissions
from rest_framework.response import Response
from account import views
from . import serializers
from account.permissions import IsAuthor, IsAccountOwner
from .models import Comment, Like, Favorites
from .serializers import FavoritesSerializer, LikeSerializer
from rest_framework import permissions as per

User = get_user_model()


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor)


class FavoritesView(views.APIView):
    permission_classes = (IsAccountOwner,)

    def get(self, request):
        user = request.user
        favorites = user.favorites.all()
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)


class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions, IsAuthenticated,)
    serializer_class = serializers.LikeSerializer

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.action = None

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



    def get_permissions(self):
        # создавать может только залогиненный юзер
        if self.action in ('create', 'add_to_liked', 'remove_from_liked', 'get_likes',):
            return [permissions.IsAuthenticated()]
        # изменять и удалять может только исполнитель
        elif self.action in ('update', 'partial_update', 'destroy',):
            return [permissions.IsAccountOwner()]
        # Просматривать могут все
        else:
            return [permissions.AllowAny()]

    #
    # def get_serializer_class(self):
    #     if self.request.method in ('PUT', 'PATCH', 'DELETE'):
    #         return [permissions.IsAuthenticated(), IsAuthor]
    #     return [permissions.AllowAny()]
    #
    # def get_permissions(self):
    #     if self.request.method in ('PUT', 'PATCH'):
    #         return serializers.LikeCreateSerializer
    #     return serializers.LikeSerializer



    @action(['POST'], detail=True, )
    def add_to_liked(self, request, pk):
        music = self.get_object()
        if request.user.liked.filter(music=music).exists():
            return response.Response("Вы уже поставили лайк", status=400)
        Like.objects.create(music=music, owner=request.user)
        return response.Response('Вы поставили лайк', status=201)

    @action(['POST'], detail=True, )
    def remove_from_liked(self, request, pk):
        music = self.get_object()
        if request.user.liked.filter(music=music).exists():
            return response.Response("Вы не лайклаи этот пост", status=400)
        request.user.liked.filter(music=music).delete()
        return response.Response("Ваш лайк удален", status=204)

    @action(['GET'], detail=True, )
    def get_likes(self, request):
        music = self.get_object()
        likes = music.likes.all()
        serializer = LikeSerializer(likes, many=True)
        return response.Response(serializer.data, status=200)

    @action(['POST'], detail=True)
    def favorite(self, request, pk):
        music = self.get_object()
        if request.user.favorites.filter(music=music).exists():
            request.user.favorites.filter(music=music).delete()
            return response.Response("Убрано из избранных", status=204)
        Favorites.objects.create(music=music, owner=request.user)
        return response.Response("Добавлено в избранные", status=201)


    # @action(['GET', 'POST'], detail=True)
    # def reviews(self, request, pk=None):
    #     music = self.get_object()
    #     if request.method == 'GET':
    #         reviews = music.reviews.all()
    #         serializer = ReviewSerializer(data=data, context={'request': request, 'music': music})
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return response.Response(serializer.data, status=201)