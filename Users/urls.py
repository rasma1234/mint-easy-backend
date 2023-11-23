from django.urls import path
from .views import GoogleLogin, FacebookConnect, TwitterConnect, UserListView, UserDetailView

urlpatterns = [

    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('dj-rest-auth/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('dj-rest-auth/twitter/connect/', TwitterConnect.as_view(), name='twitter_connect'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]