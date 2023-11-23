# from rest_framework import serializers
# from dj_rest_auth.serializers import UserDetailsSerializer

# # class UserProfileSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = UserProfile
# #         fields = ('company_name',)

# class UserSerializer(UserDetailsSerializer):

#     profile = UserProfileSerializer(source="userprofile")

#     class Meta(UserDetailsSerializer.Meta):
#         fields = UserDetailsSerializer.Meta.fields + ('profile',)

#     def update(self, instance, validated_data):
#         userprofile_serializer = self.fields['profile']
#         userprofile_instance = instance.userprofile
#         userprofile_data = validated_data.pop('userprofile', {})

#         # to access the 'company_name' field in here
#         # company_name = userprofile_data.get('company_name')

#         # update the userprofile fields
#         userprofile_serializer.update(userprofile_instance, userprofile_data)

#         instance = super().update(instance, validated_data)
#         return instance

from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class UserListView(serializers.ListSerializer):
    child = UserDetailsSerializer()

class UserDetailView(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ('id', 'username', 'email')
