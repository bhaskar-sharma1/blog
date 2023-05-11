from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class BlogsCategory(models.Model):
    '''
    '''
    category_name = models.CharField(max_length=200,null=True,blank=True,unique=True)
    category_image = models.ImageField(upload_to='logo/',null=True,blank=True)

    def __str__(self):
        return self.category_name

class Blogs(models.Model):
    '''
    '''
    category = models.ForeignKey(BlogsCategory,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='blog/',null=True,blank=True)
    about = models.CharField(max_length=500,null=True,blank=True)
    title = models.CharField(max_length=500,null=True,blank=True)
    body = RichTextUploadingField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

