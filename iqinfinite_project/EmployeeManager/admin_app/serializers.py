from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from auth_user.models import *
import re

# READ ONLY API STARTS
class UserSerializer(serializers.ModelSerializer):
    '''
    class UserProfile(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
        
        here role_name = source='profile.role_name' means It's refering to the UserProfile model 
        since the related_name = 'profile'
    '''
    role_name = serializers.CharField(source='profile.role_name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role_name']

class UserProfileSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'role', 'role_name','is_deleted','is_active','created_by','updated_by','created_at','updated_at']

class GetAllUsersSerializers(serializers.ModelSerializer):
    # here source = 'profile ' because in user profile model --> user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    user_profile = UserProfileSerializer(source='profile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'user_profile']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # print(data)  # Print serialized data for debugging
        return data
# READ ONLY API ENDS

# UPDATE USER FORM RELATED SERIALIZERS 
class UpdateUserProfileSeirlaizer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields = ['user','role','role_name','is_deleted']

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']    
# UPDATE USER FORM RELATED SERIALIZERS 

class SetUserIsActiveSerializer(serializers.Serializer):
    user_pk = serializers.IntegerField()
    def validate(self,data):
        if data.get('user_pk') <= 0:
            raise serializers.ValidationError("primary key for User cannot be zero or a negative number")
        return data

class SetUserIsDeletedSerializer(serializers.Serializer):
    user_pk = serializers.IntegerField()
    def validate(self,data):
        if data.get('user_pk') <=0:
            raise serializers.ValidationError("primary key for User cannot be zero or a negative number")
        return data
    