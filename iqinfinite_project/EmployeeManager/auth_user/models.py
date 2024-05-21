from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserRole(models.Model):
    role_name = models.CharField(max_length=50)
    def __str__(self):
        return self.role_name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole,on_delete=models.PROTECT,null=True,blank=True)
    role_name = models.CharField(max_length=50,null=True,blank=True)
    # add profile picture imagefield
    def __str__(self):
        return self.role_name
