from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from auth_user.models import *
import re

# MANAGE USERS PAGE RELATED SERIALIZERS STARTS
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
        fields = ['id', 'username', 'first_name', 'last_name', 'role_name','is_superuser']

class UserProfileSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    superior = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['id', 'role', 'role_name','is_deleted','is_active','created_by','updated_by','created_at','updated_at','superior']

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
    
class ChangeUserPasswordSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    def validate(self, data):
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
        # remove password2 from validated data
        data.pop('password2')
        return data
    
    def update(self, user_instance,validated_data):
        user_instance.set_password(validated_data['password'])
        user_instance.save()
        return user_instance
# MANAGE USERS PAGE RELATED SERIALIZERS ENDS

# ASSIGN USERS RELATED SERIALIZERS STARTS
class GetAllManagerSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='profile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'user_profile']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Print serialized data for debugging if needed
        return data

class AssignHrToMagagerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    selected_hrs = serializers.ListField(
        child=serializers.DictField()
    )

    def create(self,validated_data):
        user_id = validated_data.get('user_id')
        selected_hrs_data = validated_data.get('selected_hrs')
        # Update each HR's superior to the selected manager
        for hr_data in selected_hrs_data:
            hr_user_id = hr_data['id']
            UserProfile.objects.filter(user = hr_user_id).update(
                superior = user_id
            )
        return validated_data

class RemoveHrFromMagagerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    removed_hrs = serializers.ListField(
        child = serializers.DictField()
    )

    def create(self,validated_data):
        removed_hrs = validated_data.get('removed_hrs')
        superuser = User.objects.get(is_superuser = True)
        for removed_hr in removed_hrs:
            hr_user_id = removed_hr['id']
            UserProfile.objects.filter(user = hr_user_id).update(
                superior = superuser
            )
        return validated_data
# ASSIGN USERS RELATED SERIALIZERS ENDS