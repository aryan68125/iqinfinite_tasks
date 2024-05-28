from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserRole(models.Model):
    role_name = models.CharField(max_length=50)
    def __str__(self):
        return self.role_name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    role = models.ForeignKey(UserRole,on_delete=models.PROTECT,null=True,blank=True)
    role_name = models.CharField(max_length=50,null=True,blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    is_blocked = models.BooleanField(default=False,null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_profiles')
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='updated_profiles')
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)
#  put default value of updated_by and created_by is 29
    # add profile picture imagefield
    def __str__(self):
        return self.role_name
