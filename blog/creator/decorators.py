from .models import Blogs
from django.shortcuts import redirect

def is_blog_valid(function):
    """
        
    """    
    def wrap(request, *args, **kwargs):
        blog_id = kwargs["blog_id"]
        user_id = request.user.id
        print(blog_id,'  ',user_id)
        blog =Blogs.objects.filter(pk=blog_id,author=user_id)    
        if blog:            
            print("ture")
            return function(request, *args, **kwargs)            
        else:
            print("ture")
            return redirect('home')
    return wrap