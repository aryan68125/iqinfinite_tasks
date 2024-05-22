from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class RegisterUserPage(TemplateView):
    template_name = 'auth_user/register_user.html'

class VerifyOtpPage(TemplateView):
    template_name = 'auth_user/verify_otp_page.html'

class LoginPage(TemplateView):
    template_name = 'auth_user/login_page.html'