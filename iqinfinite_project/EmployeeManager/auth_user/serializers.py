from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from auth_user.models import *

# CUSTOM VALIDATION FOR USER PROFILE SERIALIZER STARTS
# def validate_user_role(value):
#     if value == -1:
#         raise serializers.ValidationError("User role can not be empty \n Select the user role and try again.")
# CUSTOM VALIDATION FOR USER PROFILE SERIALIZER ENDS

class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from validated data
        validated_data['is_active'] = False
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user','role','role_name']

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRole
        fields = ['id','role_name']

class VerifyOTPSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=200)
    def validate_otp(self,value):
        if value == "":
            raise serializers.ValidationError("OTP can't be empty")
        return value