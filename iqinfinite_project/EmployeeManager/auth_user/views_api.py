#database related imports
from django.db import IntegrityError

#django auth related imports
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.shortcuts import render
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
'''cross origin api'''   
class ReadUserRoles(APIView):
    def get(self,request):
        user_role = UserRole.objects.all()
        serializer = UserRoleSerializer(user_role,many=True)
        return Response({'status':200,'data':serializer.data},status=200)
# GET USER ROLES FROM DB ENDS

# COMPLETE USER AUTHENTICATION STARTS
# USER REGISTER APIS STARTS
OTP_backup = {}
Email_Data_backup = {}
User_backup = {}
'''cross origin api'''    
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
            
'''cross origin api'''    
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
# USER REGISTER APIS ENDS

# USER LOGIN/LOGOUT APIS STARTS
'''
This class handles the login of the user when the request originates from the same origin 
(i.e : If you use fetch api from a js file attched to a html file rendered by the django
project on which that fetch api is hitting the api)
'''
'''same origin'''
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
                return Response({'status':500,'error':'Username or Password not correct'},status=500)
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
'''same origin'''
class LogoutSameOrigin(APIView):
    def get(self,request):
        print("Logout button pressed")
        logout_user(request)
        return Response({'status':200,'msg':"Logout button pressed"},status=200)
    
'''cross origin'''
# from rest_framework_simplejwt.tokens import RefreshToken
class LogoutView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
         try:
              refresh_token = request.data["refresh_token"]
              token = RefreshToken(refresh_token)
              token.blacklist()
              return Response({'status':205,'msg':'user logged out refresh token reset'},status=205)
         except Exception as e:
              return Response({'status':400,'error':str(e)},status=400)
# USER LOGIN/LOGOUT APIS ENDS
    
# USER FORGOT PASSWORD APIS STARTS
'''cross origin api'''    
class ForgotPassword(APIView):
    def post(self,request):
        print(request.data)
        serializer = ForgotPasswordSerializers(data = request.data)
        if serializer.is_valid():
            email = request.data['email']
            print(email)
            try:
                user = User.objects.get(email = email)
                uid= urlsafe_base64_encode(force_bytes(user.id))
                print(f"encoded uid : {uid}")
                token = PasswordResetTokenGenerator().make_token(user)
                print(f"password reset token : {token}")
                # NOTE make this link dynamic '''http://127.0.0.1:8000/''' NOTE 
                current_site = get_current_site(request).domain
                relaive_link = reverse('PasswordTokenCheck',kwargs={'uid':uid,'token':token})
                link = f'http://{current_site}/{relaive_link}' #this link will open the  reset_password page
                print(f"generated reset password link : {link}")

                #send otp via email here
                # Prepare email
                lint_to_send = link
                email_addr = user.email
                username = user.username
                subject = f"{username} please reset your password"
                message = f"Reset Password by clicking this link : {lint_to_send}"
                recipient_list = [email_addr]

                send_email_task.delay(subject, message, EMAIL_HOST_USER, recipient_list)
                return Response({'status':200,'context':email,'msg':'Reset password link sent to you email'},status=200)
            except User.DoesNotExist:
                return Response({'status':500,'error':'User does not exist'},status=500)
            except Exception as e:
                return Response({'status':500,'error':str(e)},status=500)
        else:
            print(serializer.errors)
            if 'email' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['email'][0]},status=400)
            else:
                return Response({'status':400,'error':'Comething went wrong'},status=400)
            
'''cross origin api'''    
class PasswordTokenCheck(APIView):
    def get(self,request,uid,token):
        try:
            id = smart_str(urlsafe_base64_decode(uid))
            try:
                user = User.objects.get(id = id)
                if not PasswordResetTokenGenerator().check_token(user,token):
                    return Response({'status':500,'error':'token mis-match'},status=500)
                else:
    
                    return Response({'status':200,'msg':'Password reset success','uid':uid,'token':token},status=200)
            except User.DoesNotExist:
                return Response({'status':404,'error':'User does not exist'},status=404)
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'status':500,'error':'Token is not valid please try a new one'},status=500)

'''
This class handles the ForgotPassword when reseting the password of the user when the request originates from the same origin 
(i.e : If you use fetch api from a js file attched to a html file rendered by the django
project on which that fetch api is hitting the api)
'''
'''same origin'''
class ForgotPasswordSameOrigin(APIView):
    def post(self,request):
        print(request.data)
        serializer = ForgotPasswordSerializers(data = request.data)
        if serializer.is_valid():
            email = request.data['email']
            print(email)
            try:
                user = User.objects.get(email = email)
                uid= urlsafe_base64_encode(force_bytes(user.id))
                print(f"encoded uid : {uid}")
                token = PasswordResetTokenGenerator().make_token(user)
                print(f"password reset token : {token}")
                # NOTE make this link dynamic '''http://127.0.0.1:8000/''' NOTE 
                current_site = get_current_site(request).domain
                relaive_link = reverse('PasswordTokenCheckSameOrigin',kwargs={'uid':uid,'token':token})
                link = f'http://{current_site}/{relaive_link}' #this link will open the  reset_password page
                print(f"generated reset password link : {link}")

                #send otp via email here
                # Prepare email
                lint_to_send = link
                email_addr = user.email
                username = user.username
                subject = f"{username} please reset your password"
                message = f"Reset Password by clicking this link : {lint_to_send}"
                recipient_list = [email_addr]

                send_email_task.delay(subject, message, EMAIL_HOST_USER, recipient_list)
                return Response({'status':200,'context':email,'msg':'Reset password link sent to you email'},status=200)
            except User.DoesNotExist:
                return Response({'status':500,'error':'User does not exist'},status=500)
            except Exception as e:
                return Response({'status':500,'error':str(e)},status=500)
        else:
            print(serializer.errors)
            if 'email' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['email'][0]},status=400)
            else:
                return Response({'status':400,'error':'Comething went wrong'},status=400)
'''
This class handles the PasswordTokenCheck when reseting the password of the user when the request originates from the same origin 
(i.e : If you use fetch api from a js file attched to a html file rendered by the django
project on which that fetch api is hitting the api)
'''
'''same origin'''
class PasswordTokenCheckSameOrigin(APIView):
    def get(self,request,uid,token):
        try:
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id = id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({'status':500,'error':'token mis-match'},status=500)
            else:
                return render(request, 'auth_user/reset_password_page.html', {'uid': uid, 'token': token})
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'status':500,'error':'Token is not valid please try a new one'},status=500)

'''cross origin'''
class ResetPassword(APIView):
    def patch(self,request):
        serializer = ResetPasswordSerializer(data=request.data)
        # TODO video link : https://github.com/aryan68125/iqinfinite_tasks/tree/e9d5b6be2ccdc6193723c306dc2f61ea774889ed/iqinfinite_project/EmployeeManager	
        # TODO django_framework 101 page no 305
        print(f"before serializer is valid : {request.data}")
        if serializer.is_valid():
            uid = request.data['uid']
            token = request.data['token']
            try:
                id = smart_str(urlsafe_base64_decode(uid))
                try:
                    user = User.objects.get(id = id)
                    print(f"after serializer is valid : {request.data}")
                    if not PasswordResetTokenGenerator().check_token(user,token):
                        return Response({'status':500,'error':'Token mis-match try again with a new reset link'},status=500)
                    else:
                        user.set_password(request.data['password'])
                        user.save()
                        return Response({'status':200,'msg':'Password reset'},status=200)
                except User.DoesNotExist:
                    return Response({'status':404,'error':'User does not exist'},status=404)
            except DjangoUnicodeDecodeError as identifier:
                if not PasswordResetTokenGenerator().check_token(user):
                    return Response({'status':500,'error':'Token is not valid please try a new one'},status=500)
        else:
            print(serializer.errors)
            if 'password' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['password']},status=400)
            if 'password2' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['password2']},status=400)
            if 'uid' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['uid']},status=400)
            if 'token' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['token']},status=400)
            if 'non_field_errors' in serializer.errors:
                return Response({'status':400,'error':serializer.errors['non_field_errors']},status=400)
# USER FORGOT PASSWORD APIS ENDS

# COMPLETE USER AUTHENTICATION ENDS

# TESTING USER LOGIN VIA HOMEPAGE DUMMY API START
'''
supports cross-origin and same-origin requests
'''
class HomeLoginTester(APIView):
    authentication_classes = (JWTAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        if request.user.id:
            user_id = request.user.id
            print(f"cross-origin api call client bruno : {user_id}")
            try:
                user = User.objects.get(id=user_id)
                username = user.username
                email = user.email
                user_profile = UserProfile.objects.get(user=user)
                user_role = user_profile.role.role_name
                user_data = {
                    'username':username,
                    'email':email,
                    'user_role':user_role,
                }
                return Response({'status':200,'msg':'User successfully logged in to Home page tester api','user_data':user_data},status=200)
            except User.DoesNotExist:
                return Response({'status':404,'error':'User not found'},status=404) 
            except UserProfile.DoesNotExist:
                user = User.objects.get(id=user_id)
                username = user.username
                email = user.email
                if user.id == 29:
                    user_data = {
                        'username':username,
                        'email':email,
                        'role':'admin'
                    }
                    return Response({'status':200,'msg':'User successfully logged in to Home page tester api','user_data':user_data},status=200) 
                else:
                    return Response({'status':404,'error':'User profile not found'},status=404)
        else:
            user_id = request.data['user_id']
            print(f"same-origin api call client fetch api : {user_id}")
            try:
                user = User.objects.get(id=user_id)
                username = user.username
                email = user.email
                user_profile = UserProfile.objects.get(user=user)
                user_role = user_profile.role.role_name
                user_data = {
                    'username':username,
                    'email':email,
                    'user_role':user_role,
                }
                return Response({'status':200,'msg':'User successfully logged in to Home page tester api','user_data':user_data},status=200)
            except User.DoesNotExist:
                return Response({'status':404,'error':'User not found'},status=404) 
            except UserProfile.DoesNotExist:
                user = User.objects.get(id=user_id)
                username = user.username
                email = user.email
                if user.id == 29:
                    user_data = {
                        'username':username,
                        'email':email,
                        'role':'admin'
                    }
                    return Response({'status':200,'msg':'User successfully logged in to Home page tester api','user_data':user_data},status=200) 
                else:
                    return Response({'status':404,'error':'User profile not found'},status=404)
# TESTING USER LOGIN VIA HOMEPAGE DUMMY API ENDS