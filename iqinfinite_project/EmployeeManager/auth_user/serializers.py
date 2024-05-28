from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from auth_user.models import *
import re

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
        fields = ['id', 'user', 'role', 'role_name', 'is_deleted', 'is_active', 'created_by', 'updated_by', 'created_at', 'updated_at']
        # read_only_fields = ['created_by', 'updated_by']

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
    
class ForgotPasswordSerializers(serializers.Serializer):
    email = serializers.EmailField()
    def validate_email(self,value):
        if value == "":
            raise serializers.ValidationError("Email field can not be Empty")
        return value

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)
    uid = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length = 255)
    def validate(self,data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password do not match")
        
        # Check if password has minimum 6 characters
        if len(password) < 6:
            raise serializers.ValidationError("Password must be greater than 6 characters")
        
        # Check if password contains at least one letter, one number, and one "@" character
        if not re.search(r'[a-zA-Z]', password):
            raise serializers.ValidationError("Password must contain alphabets")
        if not re.search(r'\d', password):
            raise serializers.ValidationError("Password must contain numbers")
        if not re.search(r'[@]', password):
            raise serializers.ValidationError("Password must contain @")
        return data
    
