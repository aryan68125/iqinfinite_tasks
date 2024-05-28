#database related imports
from django.db import IntegrityError

#django auth related imports
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.shortcuts import render,redirect
#reset User password related imports
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# NOTE make this link dynamic '''http://127.0.0.1:8000/''' in ForgotPassword class (APIView) NOTE 
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

#django rest framework related imports
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
# for cross-origin api support
from rest_framework_simplejwt.authentication import JWTAuthentication
#for same-origin api support for fetch api clients
from rest_framework.authentication import SessionAuthentication
# for logging out users using JWT for cross-origin logout api
from rest_framework_simplejwt.tokens import RefreshToken

# utitlities related imports
import re

# email related imports
import random
from EmployeeManager.settings import EMAIL_HOST_USER
#send mail tasks (celery)
from auth_user.tasks import *

#serilaizers related imports
from admin_app.serializers import *

'''
cross origin
'''
class GetAllUsers(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def get(self,request):
        user = User.objects.exclude(is_superuser = True)
        serializer = GetAllUsersSerializers(user,many=True)
        return Response({'status':200,'data':serializer.data},status=200)

'''
cross origin
'''
class SetUserIsActive(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def patch(self,request):
        serializer = SetUserIsActiveSerializer(data=request.data)
        if serializer.is_valid():
            print(f"user_pk from font-end : {request.data['user_pk']}")
            user_pk = int(request.data['user_pk'])
            try:
                user = User.objects.get(id=user_pk)
                print(f"SetUserIsActive User object : {user}")
                print(f"SetUserIsActive user.is_active status before update: {user.is_active}")
                user.is_active = not user.is_active
                user.save()
                user_profile = UserProfile.objects.get(user=user)
                print(f"SetUserIsActive user_profile.is_active status before update: {user_profile.is_active}")
                user_profile.is_active = user.is_active
                user_profile.save()
                print(f"SetUserIsActive user.is_active status after update: {user.is_active}")
                print(f"SetUserIsActive user_profile.is_active status after update: {user_profile.is_active}")
                return Response({'status':200,'msg':'User active status updated'},status=200)
            except Exception as e:
                return Response({'status':500,'error':str(e)},status=500) 
        else:
            print(f"SetUserIsActive serializer.errors : {serializer.errors}")
            if 'user_pk' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['user_pk']},status=400)
            else:
                return Response({'status':400,'error':serializer.errors},status=400)

