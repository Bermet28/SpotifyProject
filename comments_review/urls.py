from django.urls import path
from . import views

urlpatterns = [
    path('comments/', ListCommentCreateView.as_view()),
    path('comments/<int:pk>', views.CommentDetailView.as_view()),
    path('favorites/', views.FavoritesView.as_view()),
]