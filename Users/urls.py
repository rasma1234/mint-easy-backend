from django.urls import path
from .views import GoogleLogin, FacebookConnect, TwitterConnect, UserListView, UserDetailView, CustomLoginView
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
urlpatterns = [

    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('dj-rest-auth/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('dj-rest-auth/twitter/connect/', TwitterConnect.as_view(), name='twitter_connect'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('dj-rest-auth/registration/account-confirm-email/<str:key>/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('dj-rest-auth/login/', CustomLoginView.as_view(), name='custom-login'),
    
]