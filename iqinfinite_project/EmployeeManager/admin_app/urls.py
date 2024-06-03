from django.urls import path,include
from admin_app.views import *
urlpatterns=[
    # path('',admin_dashboard_page,name="admin_dashboard_page"),
    path('manage_users_page/',manage_users_page,name = "manage_users_page"),
    path('manage_tasks_page/',manage_tasks_page,name="manage_tasks_page"),
    path('admin_settings_page/',admin_settings_page,name="admin_settings_page"),
    path('assign_users_page/',assign_users_page,name="assign_users_page"),
    path('api/',include('admin_app.urls_api')),
]