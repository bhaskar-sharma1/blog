from .models import BlogsCategory,Blogs
from django.contrib.auth.models import User
import os


def category_list():
    '''
        RETURN ALL BLOG CATEGORY LIST
    '''
    try:
        categories = BlogsCategory.objects.all()
        return categories
    except Exception as e:
        pass

def save_blog(request):
    '''
        SAVE BLOG DATA
    '''
    try:
        print("hello")
        blog_id = request.POST.get('blog_id',None)
        print("blog id >> ",blog_id)
        category_id = request.POST.get('category',None)
        title = request.POST.get('title',None)
        about = request.POST.get('about',None)
        description = request.POST.get('description',None)
        cover_image = request.FILES['cover_image'] if request.FILES else ''
        print("cover image ",cover_image)
        print(blog_id,category_id,title,about,description,cover_image)
        print('descript ion >> ',description)
        if blog_id:
            print("blog id >> ",blog_id)
            blog = Blogs.objects.get(id=blog_id)
            blog.author = request.user
            blog.title = title
            blog.about = about
            blog.cover_image = cover_image
            blog.body = description
            blog.save()
        else:
            print(request.user)
            blog = Blogs.objects.create(category_id=category_id,author=request.user,title=title,about=about,cover_image=cover_image,body=description)
            blog_id = blog.id
            blog.save()
        return {'blog_id':blog_id}
    except Exception as e:
        pass

def my_blog_list(user_id):
    '''
        RETURN A USER BLOG LIST
    '''
    try:
        blog_list = Blogs.objects.filter(author=user_id)
        print("blog list ",blog_list)
        return blog_list
    except Exception as e:
        pass

def blog_info(id):
    '''
        RETURN A PARTICULAR BLOG INFORMATION
    '''
    try:
        if id:
            blog = Blogs.objects.get(id=id)
        else:
            blog = ''
        return blog
    except Exception as e:
        pass

def all_blogs(param):
    '''
        RETURN ALL BLOGS
    '''
    try:
        if param == 'all':
            categories = BlogsCategory.objects.all()
            blog = Blogs.objects.all()
        return {'categories':categories,'blogs':blog}
    except Exception as e:
        pass

def edit_blog(blog_id,user_id):
    '''
        GET BLOG DATA FOR WHILE EDITING
    '''
    try:
        if blog_id and user_id:
            category = BlogsCategory.objects.all()
            blog = Blogs.objects.get(id=blog_id)
            return {'categories':category,'blog':blog}
    except Exception as e:
        pass

def delete_blog(request,blog_id):
    '''
    '''
    try:
        if blog_id and request.user:
            blog = Blogs.objects.get(id=blog_id,author=request.user)
            blog.delete()
            return {'message':'Blog has been deleted'}
    except Exception as e:
        pass