# user = test password = test
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.social_serializers import TwitterConnectSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from allauth.account.models import EmailAddress
from dj_rest_auth.views import UserDetailsView
from .serializers import UserListView, UserDetailView
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import generics
from django.contrib.auth.models import User
#from .permissions import CustomLoginSerializer
from django.views.decorators.csrf import csrf_protect
from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter

class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter

class UserListView(ListCreateAPIView):
    #queryset = User.objects.all()
    #permission_classes = (IsAuthorOrReadOnly, )
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


@method_decorator(csrf_protect, name='dispatch')
class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = request.user
        if not user.emailaddress_set.filter(verified=True).exists():
            logout(request)
            return Response(
                {'detail': 'Email not verified.'},
                status=status.HTTP_403_FORBIDDEN  # 403 Forbidden
            )

        return response


@method_decorator(csrf_protect, name='dispatch')
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

            custom_data = {'message': 'The User ist registered and the E-Mail is sended.'}
            response.data = response.data or {}
            response.data.update(custom_data)

        return response


import requests
from datetime import datetime
from django.db import models

# Assuming ForexData is your Django model
#from your_app.models import ForexData

def fetch_forex_data(api_token):
    api_endpoint = 'YOUR_API_ENDPOINT'
    
    try:
        # Set up the headers with the Bearer token
        headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json',
        }

        # Make a GET request to the API with headers
        response = requests.get(api_endpoint, headers=headers)
        response.raise_for_status()

        forex_data_list = response.json()

        for forex_data in forex_data_list:
            ForexData.objects.create(
                symbol=forex_data['symbol'],
                datetime=datetime.strptime(forex_data['datetime'], '%Y-%m-%dT%H:%M:%SZ'),
                current_price=forex_data['current_price'],
                open_price=forex_data['open_price'],
                close_price=forex_data['close_price'],
                high_price=forex_data['high_price'],
                low_price=forex_data['low_price'],
                percent_change=forex_data['percent_change'],
            )

        print('Data successfully fetched and stored in the database.')

    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')

if __name__ == '__main__':
    # Replace 'YOUR_API_ENDPOINT' and 'YOUR_API_TOKEN' with your actual API endpoint and token
    api_endpoint = 'YOUR_API_ENDPOINT'
    api_token = 'YOUR_API_TOKEN'

    fetch_forex_data(api_token)
