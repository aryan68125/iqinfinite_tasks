#database related imports
from django.db import IntegrityError

#django auth related imports
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
#reset User password related imports
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

#django rest framework related imports
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# utitlities related imports
import re

# email related imports
import random
from EmployeeManager.settings import EMAIL_HOST_USER
#send mail tasks (celery)
from auth_user.tasks import *

#serilaizers related imports
from auth_user.serializers import *

# CUSTOM USER PASSWORD VALIDATION STARTS 
def is_valid_password(password):
    # Check if password has minimum 6 characters
    if len(password) < 6:
        return False
    
    # Check if password contains at least one letter, one number, and one "@" character
    if not re.search(r'[a-zA-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@]', password):
        return False
    
    # If all conditions are met, return True
    return True
# CUSTOM USER PASSWORD VALIDATION ENDS

# GET USER ROLES FROM DB STARTS
class ReadUserRoles(APIView):
    def get(self,request):
        user_role = UserRole.objects.all()
        serializer = UserRoleSerializer(user_role,many=True)
        return Response({'status':200,'data':serializer.data},status=200)
# GET USER ROLES FROM DB ENDS

# COMPLETE USER AUTHENTICATION STARTS
OTP_backup = {}
Email_Data_backup = {}
User_backup = {}
class RegisterUser(APIView):
    def post(self,request):
        serializer = CreateUserSerializer(data=request.data)
        print(request.data)
        password1 = request.data['password']
        password2 = request.data['password2']
        email_check = request.data['email']
        try:
            # send error message in the frontend and do not save the user in the db
            user_check  = User.objects.get(email = email_check)
            return Response({'status':500,'error':'Email taken'},status=500)
        except User.DoesNotExist:
            # register user if user does not exist
            if password1 == password2:
                if is_valid_password(password1):
                    if serializer.is_valid():
                        user = serializer.save()
                        User_backup.clear()
                        User_backup.update({'user':user})
                        print(f"backed up user : {User_backup}")
                        role_id = request.data.get('role')
                        print(f"role_id : {role_id}")
                        if not role_id == "default":
                            role = UserRole.objects.get(id=role_id)
                            data = {
                                'user':user.id,
                                'role':role_id,
                                'role_name':str(role.role_name),
                            }
                            user_profile_serializer = UserProfileSerializer(data = data)
                            if user_profile_serializer.is_valid(raise_exception=True):
                                user_profile_serializer.save()
        
                                # generate otp
                                otp = random.randint(0,999999999)
                                OTP_backup.clear()
                                OTP_backup.update({"otp":otp})
                                print(f"Saved OTP : {OTP_backup}")
        
                                # send email 
                                recipient_email_address = user.email
                                username = user.username
                                user_role_id = role_id
                                Email_Data_backup.clear()
                                Email_Data_backup.update(
                                    {
                                        'username':username,
                                        'email':recipient_email_address,
                                        'role':user_role_id
                                    }
                                )
                                print(f"Saved User DATA : {Email_Data_backup}")
                                
                                try:
                                    email_addr = Email_Data_backup['email']
                                    subject = f"{Email_Data_backup['username']} please verify your email address"
                                    message = f"verify your otp : {OTP_backup['otp']}"
                                    recipient_list = [email_addr]
                                    send_email_task.delay(subject, message, EMAIL_HOST_USER, recipient_list)
                                    email_addr = ""
                                    return Response({'status':200,'msg':'Email sent'},status=200)
                                except Exception as e:
                                    return Response({'status':500,'error': str(e)},status=500)
                            else:
                                if User_backup != {}:
                                    User_backup['user'].delete()
                                return Response({'status':400,'error':str(user_profile_serializer.errors)},status=400)
                        else:
                            if User_backup != {}:
                                User_backup['user'].delete()
                            return Response({'status':400,'error':'User role not selected'},status=400)
                    else:
                        if User_backup != {}:
                            User_backup['user'].delete()
                        # email_error_message = serializer.errors.get('email', [''])[0]
                        email_error_message = serializer.errors.get('email', [])
                        # username_error_message = serializer.errors.get('username', [''])[0]
                        username_error_message = serializer.errors.get('username', [])
                        if email_error_message:
                            username_error_message = ""
                            return Response({'status': 400, 'error': email_error_message}, status=400)
                        elif username_error_message:
                            email_error_message = ""
                            return Response({'status': 400, 'error': username_error_message}, status=400)
                        else:
                            email_error_message = ""
                            username_error_message = ""
                            return Response({'status': 500, 'error': 'Unexpected error'}, status=500)
                else:
                    return Response({'status':400,'error':'Invalid password : \n 1. password must be greater than 6 characters \n 2. It must contain characters , numbers , and special characters like @'},status=400)
            else:
                if User_backup != {}:
                    User_backup['user'].delete()
                return Response({'status':400, 'error': "Password do not match"},status=400)

class VerifyOTPResendOTP(APIView):
    #VERIFY OTP
    def post(self,request):
        verify_otp_serializer = VerifyOTPSerializer(data = request.data)
        backup_otp = OTP_backup['otp']
        username = Email_Data_backup['username']
        try:
            user = User.objects.get(username=username)
            if verify_otp_serializer.is_valid():
                if user:
                    if int(request.data['otp']) == int(backup_otp):
                        print(f"otp matched :-> front-end otp : {request.data['otp']} :: backup_otp backend {backup_otp}")
                        user.is_active = True
                        user.save()
                        # activate the user account :: set is_active to True
                        return Response({'status':200,'msg':'otp verified'},status=200)
                    else:
                        return Response({'status':400,'error':'otp did not match'},status=400)
            else:
                print(verify_otp_serializer.errors['otp'][0])
                return Response({'status':400,'error':verify_otp_serializer.errors['otp'][0]},status=400)
        except User.DoesNotExist as e:
            return Response({'status':500,'error':str(e)},status=500)
        OTP_backup.clear()
    #RESEND OTP
    def get(self,request):
        # generate otp
        otp = random.randint(0,999999999)
        OTP_backup.clear()
        OTP_backup.update({"otp":otp})
        print(f"Saved OTP : {OTP_backup}")
        try:
            email_addr = Email_Data_backup['email']
            subject = f"{Email_Data_backup['username']} please verify your email address"
            message = f"verify your otp : {OTP_backup['otp']}"
            recipient_list = [email_addr]
            send_email_task.delay(subject, message, EMAIL_HOST_USER, recipient_list)
            email_addr = ""
            return Response({'status':200,'msg':'Email sent'},status=200)
        except Exception as e:
            return Response({'status':500,'error': str(e)},status=500)

'''
This class handles the login of the user when the request originates from the same origin 
(i.e : If you use fetch api from a js file attched to a html file rendered by the django
project on which that fetch api is hitting the api)
'''
class LoginSameOrigin(APIView):
    def post(self,request):
        print(request.data)
        serializer = LoginUserSerializer(data = request.data)
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            print(f"username = {username} :: password = {password}")
            user = authenticate(username=username,password=password)
            if user:
                if user.is_superuser==True:
                    return Response({'status':200,'user_role_id':1, 'user_role_name':'admin'},status=200)
                else:
                    userprofile = UserProfile.objects.get(user = user.id)
                    role_db_object = userprofile.role
                    login_user(request,user)
                    return Response({'status':200,'user_role_id':role_db_object.id,'user_role_name':role_db_object.role_name},status=200)
            else:
                return Response({'status':500,'error':'User not found'},status=500)
        else:
            # NOTE TODO TAKE NOTES ON HOW TO CHECK FOR KEYS IN A DICTIONARY CONTAINING SERIALIZER ERRORS TODO NOTE
            if 'username' in serializer.errors:
                print(f"username == {serializer.errors['username']}")
                return Response({'status':400,'error':serializer.errors['username']},status=400)
            elif 'password' in serializer.errors:
                print(f"password_error == {serializer.errors['password']}")
                return Response({'status':400,'error':serializer.errors['password']},status=400)
            else:
                return Response({'status':400,'error':serializer.errors},status=400)
'''
This class handles the logout of the user when the request originates from the same origin 
(i.e : If you use fetch api from a js file attched to a html file rendered by the django
project on which that fetch api is hitting the api)
'''
class LogoutSameOrigin(APIView):
    def get(self,request):
        print("Logout button pressed")
        logout_user(request)
        return Response({'status':200,'msg':"Logout button pressed"},status=200)
    
class ForgotPassword(APIView):
    def post(self,request):
        pass
# COMPLETE USER AUTHENTICATION ENDS