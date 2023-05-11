from django.shortcuts import render,redirect
from . import database as db
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import is_blog_valid

# Create your views here.
def home(request):
    try:
        data = db.all_blogs('all')
        return render(request,'home.html',data)
    except Exception as e:
        pass

@login_required(login_url='sign_in')
def add_blog(request):
    '''
    '''
    try:
        if request.method == 'GET':
            categories = db.category_list()
            return render(request,'add_blog.html',{'categories':categories})
        else:
            response = db.save_blog(request)
            print("response >> ",response)
            messages.success(request, 'Blog added successfully.')
            return redirect('blog',response['blog_id'])
    except Exception as e:
        pass

@login_required(login_url='sign_in')
@is_blog_valid
def edit_blog(request,blog_id=None):
    '''
    '''
    try:
        if request.method == 'GET':
            user_id = request.user.id
            data = db.edit_blog(blog_id,user_id)
            print('data',data)
            return render(request,'edit_blog.html',data)
        else:
            print("inside post edit form ")
            response = db.save_blog(request)
            print("response >. ",response)
            messages.success(request, 'Blog edited successfully.')
            return redirect('blog',response['blog_id'])
    except Exception as e:
        pass

@login_required(login_url='sign_in')
def delete_blog(request,blog_id=None):
    '''
    
    '''
    try:
        if request.method == 'GET':
            data = db.delete_blog(request,blog_id)
            messages.success(request,data['message'])
        return redirect('my_blog_list')
    except Exception as e:
        pass

@login_required(login_url='sign_in')
def my_blog_list(request):
    '''
    '''
    try:
        if request.method == 'GET':
            print("user >>> ",request.user.id)
            user_id = request.user.id
            data = db.my_blog_list(user_id)
            return render(request,'my_blogs.html',{'blogs':data})
        else:
            response = db.save_blog(request)
            return redirect('add_blog')
    except Exception as e:
        pass

def blog(request,id=None):
    '''
    '''
    try:
        if request.method == 'GET':
            print("id .. ",id)
            data = db.blog_info(id)
            return render(request,'blog_info.html',{'blog':data})
    except Exception as e:
        pass