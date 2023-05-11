from django.contrib import admin
from .models import BlogsCategory,Blogs

admin.site.register(Blogs)
admin.site.register(BlogsCategory)