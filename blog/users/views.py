from django.shortcuts import render,redirect
from django.http import JsonResponse
from . import database as db
from .decorators import to_home_page
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@to_home_page
def register(request):
    '''
    REGISTER A USER
    '''
    try:
        if request.method == 'GET':
            print("hello")
            return render(request,'register.html')
        else:
            email = request.POST.get('email')
            username =request.POST.get('username')
            password = request.POST.get('password')
            db.register_user(email,username,password)
            return redirect('sign_in')
    except Exception as e:
        pass

@to_home_page
def sign_in(request):
    '''
    TO LOGGED IN USER IN THE SYSTEM
    '''
    try:
        if request.method == 'GET':
            print("hello")
            return render(request,'login.html')
        else:
            response = db.login_user(request)
            print("response",response)
            if response["success"]==False:
                messages.success(request,'Incorrect Credentials')
                return redirect('sign_in')
            else:
                return redirect('home')
    except Exception as e:
        pass


def sign_out(request):
    '''
     LOG OUT USER
    '''
    try:
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,'You have logged out successfully')
        return redirect('sign_in')
    except Exception as e:
        pass

@login_required(login_url='sing_in')
def profile(request):
    '''
        UPDATE PROFILE INFORMATION
    '''
    try:
        if(request.method=='GET'):
            user_id = request.user.id
            data = db.profile_data(user_id)
            return render(request,'profile.html',data)
        else:
            data = db.save_profile(request)
            return redirect('profile')
    except Exception as e:
        pass


def check_username(request):
    '''
    '''
    try:
        username = request.POST.get('username')
        response = db.check_username(username)
        return JsonResponse(response)
    except Exception as e:
        pass

def check_email(request):
    '''
    '''
    try:
        email = request.POST.get('email')
        response = db.check_email(email)
        return JsonResponse(response)
    except Exception as e:
        pass
    