from django.urls import path,include
from auth_user.views import *
urlpatterns = [
    path('',RegisterUserPage.as_view(),name="RegisterUserPage"),


    path('auth_api/',include('auth_user.urls_api')),
]