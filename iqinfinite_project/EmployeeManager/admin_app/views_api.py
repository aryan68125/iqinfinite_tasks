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
from rest_framework.generics import ListAPIView
# for cross-origin api support
from rest_framework_simplejwt.authentication import JWTAuthentication
#for same-origin api support for fetch api clients
from rest_framework.authentication import SessionAuthentication
# for logging out users using JWT for cross-origin logout api
from rest_framework_simplejwt.tokens import RefreshToken

# utitlities related imports
import re
from datetime import date

# email related imports
import random
from EmployeeManager.settings import EMAIL_HOST_USER
#send mail tasks (celery)
from auth_user.tasks import *

#serilaizers related imports
from admin_app.serializers import *

# MANAGE USER PAGE RELATED API VIEWS STARTS
'''
cross origin and same-origin
This api view has two urls it can get one user if userId is provided and if userId is not provided then it will
get all the users from the database
'''
class GetAllUsersOrOneUserOrUpdateUser(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def get(self,request,userId=-1):
        if not userId == -1:
            try:
               user = User.objects.get(id=userId)
               serializer = GetAllUsersSerializers(user)
               return Response({'status': 200, 'data': serializer.data}, status=200)
            except Exception as e: 
                return Response({'status':500,'error':str(e)},status=500)
        else:
            try:
                user = User.objects.exclude(is_superuser = True)
                serializer = GetAllUsersSerializers(user,many=True)
                return Response({'status':200,'data':serializer.data},status=200)
            except Exception as e:
                return Response({'status':500,'error':str(e)},status=500)
    def patch(self,request):
        user_id = request.data['user_id']
        try:
            user = User.objects.get(id=user_id)
            user_serializer = UpdateUserSerializer(user,data=request.data,partial=True)
            user_profile = UserProfile.objects.get(user=user.id)
    
            user_role_model = UserRole.objects.get(id=request.data['role_id'])
            role_name_var = user_role_model.role_name
            role_id = request.data['role_id']
            is_deleted = request.data['is_deleted']
            data = {
                'role':role_id,
                'role_name':role_name_var,
                'is_deleted':is_deleted
            }
            user_profile_serialzier = UpdateUserProfileSeirlaizer(user_profile,data=data,partial=True)
            print(f'GetAllUsersOrOneUserOrUpdateUser <-::-> user_name = {user.username} : {user_profile.role}')
            if user_serializer.is_valid() and user_profile_serialzier.is_valid():
                user_serializer.save()
                user_profile_serialzier.save()
                user.is_active = not user_profile.is_deleted
                user_profile.is_active = user.is_active
                user_profile.updated_at = date.today()
                user.save()
                user_profile.save()
                return Response({'status':200,'msg':'User updated!'},status=200)
            else:
                error = {
                    'user_serializer':user_serializer.errors,
                    'user_profile_serialzier':user_profile_serialzier.errors,
                }
                return Response({'status':400,'error':error},status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)
'''
cross origin and same-origin
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
'''
cross-origin and same-origin
'''
class SetUserIsDeleted(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def patch(self, request):
        serializer = SetUserIsDeletedSerializer(data=request.data)
        if serializer.is_valid():
            try:
                print(f"user_pk from font-end : {request.data['user_pk']}")
                user_pk = int(request.data['user_pk'])
                user = User.objects.get(id=user_pk)
                user_profile = UserProfile.objects.get(user=user)
                print(f"SetUserIsDeleted is_deleted before update : {user_profile.is_deleted}")
                #toggle between is_deleted = True and is_deleted = False
                user_profile.is_deleted = not user_profile.is_deleted
                user.is_active = not user_profile.is_deleted
                user.save()
                user_profile.is_active = user.is_active
                user_profile.save()
                print(f"SetUserIsDeleted is_deleted after update : {user_profile.is_deleted}")
                return Response({'status':200,'msg':'User delete status updated'},status=200)
            except Exception as e:
                return Response({'status':500,'error':str(e)},status=500)
        else:
            print(f"SetUserIsDeleted serializer.errors : {serializer.errors}")
            if 'user_pk' in serializer.errors:
                return Response({'status':400,'error':serializer.errors},status=400)
            else:
                return Response({'status':400,'error':serializer.errors},status=400)
            
class ChangeUserPassword(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def patch(self,request):
        try:
            user_id = request.data['user_id']
            user = User.objects.get(id=user_id)
            serializers = ChangeUserPasswordSerializer(user,data=request.data,partial=False)
            if serializers.is_valid(): 
                serializers.save()
                return Response({'status':200,'msg':'Password Changed!'},status=200)
            else:
                print(f"ChangeUserPassword :: {serializers.errors}")
                if 'non_field_errors' in serializers.errors:
                    return Response({'status':400,'error':serializers.errors['non_field_errors']},status=400)
                if 'password' in serializers.errors or 'password2' in serializers.errors:
                    return Response({'status':400,'error':serializers.errors['password']},status=400) 
                return Response({'status':400,'error':serializers.errors},status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)
# MANAGE USER PAGE RELATED API VIEWS ENDS





# ASSIGN HR TO MANAGER STARTS
class GetAllManagersListView(ListAPIView):
    serializer_class = GetAllManagerSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def get_queryset(self):
        # Filter users by the role 'manager' in their profile
        return User.objects.filter(profile__role=3, is_active=True)
    
class GetAllHrListView(ListAPIView):
    serializer_class = GetAllManagerSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def get_queryset(self):
        # Filter users by the role 'manager' in their profile
        return User.objects.filter(profile__role=2, is_active=True)

# THIS CODE IS ARCHIVED (DO NOT DELETE) WORKING SAMPLE STARTS
# class AssignHrToManagerView(APIView):
#     authentication_classes = (JWTAuthentication, SessionAuthentication)
#     permission_classes = (IsAuthenticated, IsAdminUser)
#     def patch(self,request):
#         user_id = request.data['user_id']
#         print(user_id)
#         selected_manager = User.objects.get(id=user_id)
#         selected_hrs = request.data['selected_hrs']
#         for hr in selected_hrs:
#             print(f"hr : {hr}")
#             UserProfile.objects.filter(user = hr['id']).update(
#                 superior = selected_manager
#             )
#         return Response({'status':200,'msg':f'Hrs assigned to {selected_manager} (Manager)'},status=200)
# THIS CODE IS ARCHIVED (DO NOT DELETE) WORKING SAMPLE ENDS

class AssignHrToManagerView(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def patch(self,request):
        serializer = AssignHrToMagagerSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()  # Calls the `update` method in the serializer
                selected_manager = User.objects.get(id=request.data['user_id'])
                return Response({'status': 200, 'msg': f'Hrs assigned to {selected_manager.username} (Manager)'}, status=200)
            else:
                return Response({'status': 400, 'error': serializer.errors}, status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)

class RemoveHrFromMagagerView(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,IsAdminUser)
    def patch(self,request):
        serializers = RemoveHrFromMagagerSerializer(data=request.data)
        try:
            if serializers.is_valid():
                serializers.save()
                selected_manager = User.objects.get(id=request.data['user_id'])
                return Response({'status':200,'msg':f'Hrs removed from under {selected_manager} (Manager)'},status=200)
            else:
                return Response({'status':400,'error':serializers.errors},status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)
# ASSIGN HR TO MANAGER ENDS





# ASSIGN EMPLOYEE TO HRS STARTS
class GetAllHrsListViewEmployeeAssignToHr(ListAPIView):
    serializer_class = GetAllHrSerializerAssignemployeeToHr
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def get_queryset(self):
        # Filter users by the role 'manager' in their profile
        return User.objects.filter(profile__role=2, is_active=True)
    
class GetAllEmployeesListViewEmployeeAssignToHr(ListAPIView):
    serializer_class = GetAllEmployeesSerializersEmployeeAssignToHr
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def get_queryset(self):
        # Filter users by the role 'manager' in their profile
        return User.objects.filter(profile__role=1, is_active=True)
    
class AssignEmployeeToHrView(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    def patch(self,request):
        serializer = AssignEmployeeToHrSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()  # Calls the `update` method in the serializer
                selected_hr = User.objects.get(id=request.data['user_id'])
                return Response({'status': 200, 'msg': f'Employees assigned to {selected_hr.username} (Hr)'}, status=200)
            else:
                return Response({'status': 400, 'error': serializer.errors}, status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)
        
class RemoveEmployeeFromHrView(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,IsAdminUser)
    def patch(self,request):
        serializers = RemoveEmployeeFromHrSerializer(data=request.data)
        try:
            if serializers.is_valid():
                serializers.save()
                selected_hr = User.objects.get(id=request.data['user_id'])
                return Response({'status':200,'msg':f'Employee removed from under {selected_hr} (Hr)'},status=200)
            else:
                return Response({'status':400,'error':serializers.errors},status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)
# ASSIGN EMPLOYEE TO HRS ENDS





# (ADMIN PANEL) CHANGE ADMIN INFO STARTS
class ChangeAdminInfoView(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,IsAdminUser)
    def patch(self,request):
        try:
            user_id = request.user.id
            user = User.objects.get(id = user_id, is_superuser = True)
            serializers = ChangeAdminInfoSerializer(user,data=request.data,partial = True)
            if serializers.is_valid():
                serializers.save()
                return Response({'status':200,'msg':'Admin profile info saved'},status=200)
            else:
                print(serializers.error)
                return Response({'status':400,'error':serializers.errors},status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)
        
class GetAdminUsernameView(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self,request):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id,is_superuser = True)
            username= user.username
            user_id = user.id
            return Response({'status':200,'username':username, 'user_id':user_id},status=200)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500) 

class ChangeAdminPasswordView(APIView):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,IsAdminUser)
    def patch(self,request):  
        serializers = ChangeAdminPasswordSerializer(data=request.data)
        try:
            if serializers.is_valid():
                serializers.save()
                user_id = request.data['user_id']
                admin = User.objects.get(id = user_id)
                login_user(request,admin)
                return Response({'status':200,'msg':"Password changed!"},status=200)
            else:
                print(serializers.errors)
                if 'non_field_errors' in serializers.errors:
                    return Response({'status':400,'error':serializers.errors['non_field_errors']},status=400)
                if 'user_id' in serializers.errors:
                    return Response({'status':400,'error':serializers.errors['user_id']},status=400)
                if 'password' in serializers.errors:
                    return Response({'status':400,'error':serializers.errors['password']},status=400)
                if 'password2' in serializers.errors:
                    return Response({'status':400,'error':serializers.errors['password2']},status=400)
        except Exception as e:
            return Response({'status':500,'error':str(e)},status=500)
# (ADMIN PANEL) CHANGE ADMIN INFO ENDS