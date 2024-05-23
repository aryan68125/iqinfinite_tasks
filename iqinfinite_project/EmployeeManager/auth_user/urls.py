from django.urls import path,include
from auth_user.views import *
urlpatterns = [
    path('',register_user_page,name="RegisterUserPage"),
    path('VerifyOtpPage/',verify_otp_page,name="VerifyOtpPage"),
    path('LoginPage/',login_page,name="LoginPage"),
    path('HomePage/',home_page,name="HomePage"),
    path('auth_api/',include('auth_user.urls_api')),
]