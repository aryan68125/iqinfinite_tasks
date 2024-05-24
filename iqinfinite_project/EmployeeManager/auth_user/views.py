from django.shortcuts import render,redirect
from django.views.generic import TemplateView

# Permissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# look for a way to access these pages when user is not loggedin in case of class based views
# class RegisterUserPage(TemplateView):
#     template_name = 'auth_user/register_user.html'

def register_user_page(request):
    if not request.user.is_authenticated:
        return render(request,'auth_user/register_user.html')
    else:
        return redirect('HomePage')

# class VerifyOtpPage(TemplateView):
#     template_name = 'auth_user/verify_otp_page.html'

def verify_otp_page(request):
    if not request.user.is_authenticated:
        return render(request,'auth_user/verify_otp_page.html')
    else:
        return redirect('HomePage')

# class LoginPage(TemplateView):
#     template_name = 'auth_user/login_page.html'

def login_page(request):
    if not request.user.is_authenticated:
        return render(request,'auth_user/login_page.html')
    else:
        return redirect('HomePage')
    
def forgot_password_page(request):
    if not request.user.is_authenticated:
        return render(request,'auth_user/forgot_password_page.html')
    else:
        return redirect('HomePage')
    
def reset_password_page(request):
    if not request.user.is_authenticated:

        return render(request,'auth_user/reset_password_page.html')
    else:
        return redirect('HomePage')

# class HomePage(TemplateView):
#     template_name = 'auth_user/home_page.html'
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

def home_page(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        data = {
            'user_id':user_id
        }
        return render(request,'auth_user/home_page.html',{'context':data})
    else:
        return redirect('LoginPage')
    
