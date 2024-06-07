from django.urls import path
from admin_app.views_api import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('GetAllUsers/',GetAllUsersOrOneUserOrUpdateUser.as_view(),name="GetAllUsers"),
    path('GetOneUser/<int:userId>/', GetAllUsersOrOneUserOrUpdateUser.as_view(), name='GetOneUser'),
    path('UpdateUser/', GetAllUsersOrOneUserOrUpdateUser.as_view(), name='UpdateUser'),
    path('SetUserIsActive/',SetUserIsActive.as_view(),name="SetUserIsActive"),
    path('SetUserIsDeleted/',SetUserIsDeleted.as_view(),name="SetUserIsDeleted"),
    path('ChangeUserPassword/',ChangeUserPassword.as_view(),name="ChangeUserPassword"),

    path('GetAllManagersListView/',GetAllManagersListView.as_view(),name="GetAllManagersListView"),
    path('GetAllHrListView/',GetAllHrListView.as_view(),name="GetAllHrListView"),
    path('AssignHrToManagerView/',AssignHrToManagerView.as_view(),name="AssignHrToManagerView"),
    path('RemoveHrFromMagagerView/',RemoveHrFromMagagerView.as_view(),name="RemoveHrFromMagagerView"),

    path('GetAllHrsListViewEmployeeAssignToHr/',GetAllHrsListViewEmployeeAssignToHr.as_view(), name="GetAllHrsListViewEmployeeAssignToHr"),
    path('GetAllEmployeesListViewEmployeeAssignToHr/',GetAllEmployeesListViewEmployeeAssignToHr.as_view(),name="GetAllEmployeesListViewEmployeeAssignToHr"),
    path('AssignEmployeeToHrView/',AssignEmployeeToHrView.as_view(),name="AssignEmployeeToHrView"),
    path('RemoveEmployeeFromHrView/',RemoveEmployeeFromHrView.as_view(),name="RemoveEmployeeFromHrView"),

    path('GetAdminUsernameView/',GetAdminUsernameView.as_view(),name="GetAdminUsernameView"),
    path('ChangeAdminInfoView/',ChangeAdminInfoView.as_view(),name="ChangeAdminInfoView"),
    path('ChangeAdminPasswordView/',ChangeAdminPasswordView.as_view(),name="ChangeAdminPasswordView"),
    path('UploadAdminProfilePictureView/',UploadAdminProfilePictureView.as_view(),name="UploadAdminProfilePictureView"),
]