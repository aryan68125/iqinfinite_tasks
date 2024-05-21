from django.db import IntegrityError

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
        if password1 == password2:
            if serializer.is_valid():
                user = serializer.save()
                User_backup.clear()
                User_backup.update({'user':user})
                print(f"backed up user : {User_backup}")
                role_id = request.data.get('role')
                if role_id and role_id is not 'default':
                    role = UserRole.objects.get(id=role_id)
                    data = {
                        'user':user.id,
                        'role':role_id,
                        'role_name':str(role.role_name),
                    }
                    user_profile_serializer = UserProfileSerializer(data = data)
                    if user_profile_serializer.is_valid():
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
                        
                        # send otp via celery
                        email_addr = Email_Data_backup['email']
                        subject = f"{Email_Data_backup['username']} please verify your email address"
                        message = f"verify your otp : {OTP_backup['otp']}"
                        recipient_list = [email_addr]
                        send_email_task.delay(subject, message, EMAIL_HOST_USER, recipient_list)
                        email_addr = ""
                        return Response({'status':200,'msg':'Email sent'},status=200)
                        # try:
                        #     email_addr = Email_Data_backup['email']
                        #     subject = f"{Email_Data_backup['username']} please verify your email address"
                        #     message = f"verify your otp : {OTP_backup['otp']}"
                        #     recipient_list = [email_addr]
                        #     send_email_task.delay(subject, message, EMAIL_HOST_USER, recipient_list)
                        #     email_addr = ""
                        #     return Response({'status':200,'msg':'Email sent'},status=200)
                        # except Exception as e:
                        #     return Response({'status':500,'error': str(e)},status=500)
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
            if User_backup != {}:
                User_backup['user'].delete()
            return Response({'status':400, 'error': "Password do not match"},status=400)
# COMPLETE USER AUTHENTICATION ENDS
