from django.contrib import admin
from auth_user.models import *
# Register your models here.
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin ):
    list_display = ('id', 'role_name')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role', 'created_by', 'created_at', 'updated_by' ,'updated_at','is_deleted', 'is_active')

