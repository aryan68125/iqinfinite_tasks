from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class RegisterUserPage(TemplateView):
    template_name = 'auth_user/register_user.html'
    def get_context_data(self,*args, **kwargs):
        context = super(RegisterUserPage, self).get_context_data(*args,**kwargs)
        context['title'] = "Register User"
        return context