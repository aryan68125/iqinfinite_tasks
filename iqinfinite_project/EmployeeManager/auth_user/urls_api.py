from django.urls import path

#views related imports
from auth_user.views_api import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('RegisterUser/',RegisterUser.as_view(),name="RegisterUser"),
    path('ReadUserRoles/',ReadUserRoles.as_view(),name="ReadUserRoles"),
]