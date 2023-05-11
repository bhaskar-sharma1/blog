from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuthUserExtension(models.Model):
    '''
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    profile_photo = models.ImageField(upload_to='users/',blank=True,null=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    instagram = models.CharField(max_length=500,null=True,blank=True)
    facebook = models.CharField(max_length=500,blank=True,null=True)
    youtube = models.CharField(max_length=500,null=True,blank=True)