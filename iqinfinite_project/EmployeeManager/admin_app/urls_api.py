from django.urls import path
from admin_app.views_api import *
urlpatterns = [
    path('GetAllUsers/',GetAllUsersOrOneUser.as_view(),name="GetAllUsers"),
    path('GetOneUser/<int:userId>/', GetAllUsersOrOneUser.as_view(), name='GetOneUser'),
    path('SetUserIsActive/',SetUserIsActive.as_view(),name="SetUserIsActive"),
    path('SetUserIsDeleted/',SetUserIsDeleted.as_view(),name="SetUserIsDeleted"),
]