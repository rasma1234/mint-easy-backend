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
from .permissions import IsAuthorOrReadOnly


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter

class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter

class UserListView(ListCreateAPIView):
    #queryset = User.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )
    serializer_class = UserDetailView
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(author= self.request.user)

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailView