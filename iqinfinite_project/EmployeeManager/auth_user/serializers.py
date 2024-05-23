from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from auth_user.models import *

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
    otp = serializers.IntegerField()
    def validate_otp(self,value):
        if not value:
            # this block is not working because on failiure the message below is not shown
            raise serializers.ValidationError("OTP can't be empty")
        # else:
              # # This block is working because on failiure the message below is shown
        #     if value > 5:
        #         raise serializers.ValidationError("value should not be greater than 5")
        return value
    
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=255)
    def validate(self,data):
        username = data.get('username')
        password = data.get('password')
        if username.lower() == "":
            raise serializers.ValidationError("Username must not be empty")
        if password.lower() =="":
            raise serializers.ValidationError("Password must not be empty")
        return data