#user = test password = test
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView
from dj_rest_auth.social_serializers import TwitterConnectSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from allauth.account.models import EmailAddress
from .serializers import UserListView, UserDetailView
from dj_rest_auth.serializers import UserDetailsSerializer, TokenSerializer
from rest_framework import generics, status
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.middleware.csrf import get_token


def send_csrf(request):
    return JsonResponse({"csrfToken": get_token(request)})  

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter

class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter

class UserListView(ListCreateAPIView):
    serializer_class = UserDetailView
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id= self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailView


class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        # Call the parent class's post method
        response = super().post(request, *args, **kwargs)

        # Check if the user's email is verified
        user = request.user
        if not user.emailaddress_set.filter(verified=True).exists():
            logout(request)
            return Response(
                {'detail': 'Email not verified.'},
                status=status.HTTP_403_FORBIDDEN  # 403 Forbidden
            )

        # Include user_id and auth token in the response
        user_id = user.id
        token_data = TokenSerializer(user.auth_token).data
        response_data = {'user_id': user_id, 'detail': 'Login successful', 'auth_token': token_data['key']}
        print(response_data)
        return Response(response_data, status=response.status_code)


#@method_decorator(csrf_protect, name='dispatch')
class CustomRegisterView(RegisterView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Überprüfe, ob die Response gültig ist
        if response is not None and hasattr(response, 'data'):
            send_mail(
                'Welcome to mint-easy',
                'Thank you for registration!',
                'info@mint-easy.de',
                [request.data.get('email')],
                fail_silently=False,
            )

            custom_data = {"message": "Please verify your email address."}
            response.data = response.data or {}
            response.data.update(custom_data)
            response.status_code = status.HTTP_200_OK

        return response

