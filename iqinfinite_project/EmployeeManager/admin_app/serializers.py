from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from auth_user.models import *
import re

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user', 'role','role_name']
# TODO work on this serializer
class GetAllUsersSerializers(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.profile', read_only=True)
    class Meta:
        model=User
        fields = ['id','username', 'email', 'user_profile']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data)  # Print serialized data for debugging
        return data
