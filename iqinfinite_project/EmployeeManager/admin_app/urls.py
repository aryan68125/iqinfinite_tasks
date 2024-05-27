from django.urls import path,include
from admin_app.views import *
urlpatterns=[
    # path('',admin_dashboard_page,name="admin_dashboard_page"),

    path('api/',include('admin_app.urls_api')),
]