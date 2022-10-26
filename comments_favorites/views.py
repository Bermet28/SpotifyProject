from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, response, permissions, viewsets
from rest_framework.response import Response
from account import views
from . import serializers
from account.permissions import IsAuthor, IsAccountOwner
from .models import Comment, Favorites
from .serializers import FavoritesSerializer
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


class FavoritesListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoritesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor)

    # class FavoritesView(views.APIView):
    #     permission_classes = (IsAccountOwner,)
    #
    #     def get(self, request):
    #         user = request.user
    #         favorites = user.favorites.all()
    #         serializer = FavoritesSerializer(favorites, many=True)
    #         return Response(serializer.data)
    #
    #     def get_permissions(self):
    #         if self.request.method == 'GET':
    #             return [permissions.AllowAny()]
    #         return [permissions.IsAuthenticated(), IsAuthor()]
    #
    #
    # @api_view(["POST"])
    # def add_favorites(request):
    #     serializer = FavoritesSerializer(data=request.POST)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response("Добавлено в избранные")
    #
    #
    # @api_view(["DELETE"])
    # def delete_favorites(request, c_id):
    #     comment = get_object_or_404(Comment, id=c_id)
    #     comment.delete()
    #     return Response("Удалено из избранных")

#


