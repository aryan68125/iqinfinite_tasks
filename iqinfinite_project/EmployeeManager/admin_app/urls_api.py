from django.urls import path
from admin_app.views_api import *
urlpatterns = [
    path('GetAllUsers/',GetAllUsers.as_view(),name="GetAllUsers"),
    path('SetUserIsActive/',SetUserIsActive.as_view(),name="SetUserIsActive"),
]