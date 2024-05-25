from django.urls import path

#views related imports
from auth_user.views_api import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('RegisterUser/',RegisterUser.as_view(),name="RegisterUser"),
    path('ReadUserRoles/',ReadUserRoles.as_view(),name="ReadUserRoles"),
    path('VerifyOTPResendOTP/',VerifyOTPResendOTP.as_view(),name="VerifyOTPResendOTP"),

    path('ForgotPassword/',ForgotPassword.as_view(),name="ForgotPassword"),
    path('PasswordTokenCheck/<uid>/<token>/',PasswordTokenCheck.as_view(),name="PasswordTokenCheck"),
    path('ResetPassword/',ResetPassword.as_view(),name="ResetPassword"),
    path('HomeLoginTester/',HomeLoginTester.as_view(),name="HomeLoginTester"),
    path('LogoutView/',LogoutView.as_view(),name="LogoutView"),

    path('LoginSameOrigin/',LoginSameOrigin.as_view(),name="LoginSameOrigin"),
    path('LogoutSameOrigin/',LogoutSameOrigin.as_view(),name="LogoutSameOrigin"),
    path('ForgotPasswordSameOrigin/',ForgotPasswordSameOrigin.as_view(),name="ForgotPasswordSameOrigin"),
    path('PasswordTokenCheckSameOrigin/<uid>/<token>/',PasswordTokenCheckSameOrigin.as_view(),name="PasswordTokenCheckSameOrigin"),
]

