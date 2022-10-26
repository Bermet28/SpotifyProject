from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from .views import VerifyEmail

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('refresh/', TokenRefreshView.as_view(),),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

    ]