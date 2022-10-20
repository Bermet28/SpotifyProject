from django.urls import path
from . import views
from .views import CommentListCreateView

urlpatterns = [
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('favorites/', views.FavoritesView.as_view()),
    path('likes/', views.LikeCreateView.as_view()),

]