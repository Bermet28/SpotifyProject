from django.shortcuts import render
from rest_framework import status, permissions, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .send_email import Util
from .serializers import *
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

User = get_user_model()


# Create your views here.

# TODO: register_view


class RegistrationView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response('Successfully signed up!', status=status.HTTP_201_CREATED)
        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'hhttp://' + current_site + relativeLink + "?token" + str(token)
        email_body = 'Hi' + user.username + 'Use link below to verify your email\n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass


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
