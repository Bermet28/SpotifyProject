from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .send_email import send_confirmation_email
from .serializers import *

User = get_user_model()


# Create your views here.

# TODO: register_view


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Succesfully signed up!', status=status.HTTP_201_CREATED)


# TODO: activate view
class ActivationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Successfully activated'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Link expired'}, status=400)


# TODO: login view
class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully logged out!', status=204)


# def send_mail(request):
#     html = '<html><body> Hello check your gmail</body></html>'
#     send_confirmation_email('krsymr18@gmail.com', '1234')
#     return HttpResponse(html)


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
