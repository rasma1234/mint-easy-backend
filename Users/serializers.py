# posts/serializers.py
from django.contrib.auth import get_user_model # new
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = '__all__'

