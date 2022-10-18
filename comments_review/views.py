# from django.contrib.auth import get_user_model
# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
# from rest_framework import generics, response, permissions
# from rest_framework.response import Response
# from account import views
# from . import serializers
# from account.permissions import IsAutor,
# from .models import Comment
# from .serializers import FavoriteSerializer
# User = get_user_model()
#
#  class CommentListCreateView(generics.ListCreateAPIView):
#      queryset = Comment.objects.all()
#      serializer_class = serializers.CommentSerializer
#      permission_classes = (IsAuthor,)
#
#      def perform_create(self, serializer):
#          serializer.save(owner = self.request.user)
#
# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor)
#
# class FavoritesView(views.APIView):
#     permission_classes = (IsAccountOwner,):
#     def get(self, request):
#         user = request.user
#         favorites = user.favorites.all()
#         serializer = FavoriteSerializer(favorites, many=True)
#         return Response(serializer.data)
#


