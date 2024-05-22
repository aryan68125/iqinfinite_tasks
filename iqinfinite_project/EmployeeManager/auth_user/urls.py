from django.urls import path,include
from auth_user.views import *
urlpatterns = [
    path('',RegisterUserPage.as_view(),name="RegisterUserPage"),
    path('VerifyOtpPage/',VerifyOtpPage.as_view(),name="VerifyOtpPage"),
    path('LoginPage/',LoginPage.as_view(),name="LoginPage"),
    path('auth_api/',include('auth_user.urls_api')),
]