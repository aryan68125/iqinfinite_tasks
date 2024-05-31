from django.urls import path
from admin_app.views_api import *
urlpatterns = [
    path('GetAllUsers/',GetAllUsersOrOneUserOrUpdateUser.as_view(),name="GetAllUsers"),
    path('GetOneUser/<int:userId>/', GetAllUsersOrOneUserOrUpdateUser.as_view(), name='GetOneUser'),
    path('UpdateUser/', GetAllUsersOrOneUserOrUpdateUser.as_view(), name='UpdateUser'),
    path('SetUserIsActive/',SetUserIsActive.as_view(),name="SetUserIsActive"),
    path('SetUserIsDeleted/',SetUserIsDeleted.as_view(),name="SetUserIsDeleted"),
    path('ChangeUserPassword/',ChangeUserPassword.as_view(),name="ChangeUserPassword"),
]