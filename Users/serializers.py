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

from django.conf import settings



class UserListView(serializers.ListSerializer):
    child = UserDetailsSerializer()


class UserDetailView(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ("id", "username", "email")




from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings





# class CustomPasswordResetSerializer(PasswordResetSerializer):
#     def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
#         # Get the user object from the serializer
#         user = self.user

#         # Customize the URL used in the email here
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)
#         custom_reset_url = f"http://localhost:5173/reset-password/{uid}/{token}"

#         context.update({
#             'custom_reset_url': custom_reset_url
#         })

#         send_mail(
#             subject_template_name,
#             email_template_name,
#             context,
#             from_email,
#             [to_email],
#             html_email_template_name=html_email_template_name,
#         )

        # return custom_reset_url  



