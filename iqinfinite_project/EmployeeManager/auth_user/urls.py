from django.urls import path,include
from auth_user.views import *
urlpatterns = [
    path('',register_user_page,name="RegisterUserPage"),
    path('VerifyOtpPage/',verify_otp_page,name="VerifyOtpPage"),
    path('LoginPage/',login_page,name="LoginPage"),
    path('HomePage/',home_page,name="HomePage"),
    path('forgot_password_page/',forgot_password_page,name="forgot_password_page"),
    path('reset_password_page/',reset_password_page,name="reset_password_page"),

    path('auth_api/',include('auth_user.urls_api')),
]

