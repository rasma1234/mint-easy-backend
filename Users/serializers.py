from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class UserListView(serializers.ListSerializer):
    child = UserDetailsSerializer()

class UserDetailView(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ('id', 'username', 'email')

