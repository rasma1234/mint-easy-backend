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


# from .permissions import CustomLoginSerializer
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.core.mail import send_mail
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response

from django.http import JsonResponse  # new
from django.middleware.csrf import get_token  # new


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
    # queryset = User.objects.all()
    # permission_classes = (IsAuthorOrReadOnly, )
    serializer_class = UserDetailView

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailView


# @method_decorator(csrf_protect, name="dispatch")
class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = request.user
        if not user.emailaddress_set.filter(verified=True).exists():
            logout(request)
            return Response(
                {"detail": "Email not verified."},
                status=status.HTTP_403_FORBIDDEN,  # 403 Forbidden
            )

        return response


# @method_decorator(csrf_protect, name="dispatch")
class CustomRegisterView(RegisterView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Überprüfe, ob die Response gültig ist
        if response is not None and hasattr(response, "data"):
            send_mail(
                "Welcome to mint-easy",
                "Thank you for registration!",
                "info@mint-easy.de",
                [request.data.get("email")],
                fail_silently=False,
            )

            custom_data = {"message": "Please verify your email address."}
            response.data = response.data or {}
            response.data.update(custom_data)
            response.status_code = status.HTTP_200_OK

        return response


from rest_framework.response import Response
from rest_framework import status




