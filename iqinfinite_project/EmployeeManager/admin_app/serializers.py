from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from auth_user.models import *
import re

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'role', 'role_name','is_deleted','is_blocked','created_by','updated_by','created_at','updated_at']

class GetAllUsersSerializers(serializers.ModelSerializer):
    # here source = 'profile ' because in user profile model --> user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    user_profile = UserProfileSerializer(source='profile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_profile']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data)  # Print serialized data for debugging
        return data
