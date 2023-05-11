from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *
import json
def register_user(email,username,password):
    '''
    '''
    try:
        print(email,username,password)
        user = User.objects.create(email=email,username=username)
        user.set_password(password)
        user.save()
        user_extension = AuthUserExtension.objects.create(user=user)
        user_extension.save()
        return {'success':True}
    except Exception as e:
        pass

def login_user(request):
    '''
    '''
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        exists = User.objects.filter(username=username).exists()
        if exists:
            user = authenticate(request,username=username,password=password)
            print("u >> ",user)
            if user is not None:
                login(request,user)
                return {'success':True,'message':'Login Successfully'}
            else:
                print("user not exists")
                return {'success':False,'message':'Incorrect Password'}
        else:
            return {'success':False,'message':'Incorrect Email'}
        
    except Exception as e:
        pass

def profile_data(user_id):
    '''
    '''
    try:
        user = User.objects.get(id=user_id)
        auth_user = AuthUserExtension.objects.get(user=user)
        return {'username':user.username,'first_name':user.first_name,'last_name':user.last_name,'email':user.email,'mobile':auth_user.mobile,'profile_photo':auth_user.profile_photo,'address':auth_user.address,'city':auth_user.city,'pincode':auth_user.pincode,'instagram':auth_user.instagram,'facebook':auth_user.facebook}
    except Exception as e:
        pass

def save_profile(request):
    '''
    '''
    try:
        user_id = request.user.id
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        profile_photo = request.FILES['profile_photo'] if request.FILES else ''
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        instagram = request.POST.get('instagram')
        facebook = request.POST.get('facebook')
        print("data >>> ",user_id,first_name,last_name,mobile,email,address,pincode,city,instagram,facebook)
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        auth_user =AuthUserExtension.objects.get(user=user)
        auth_user.mobile = mobile
        if profile_photo:
            auth_user.profile_photo = profile_photo
        auth_user.address = address
        auth_user.city = city
        auth_user.pincode = pincode
        auth_user.instagram = instagram
        auth_user.facebook = facebook
        auth_user.save()
        return True
    except Exception as e:
        pass

def check_username(username):
    '''
    '''
    try:
        is_exists = User.objects.filter(username=username).exists()
        return {'is_exists':is_exists}
    except Exception as e:
        pass

def check_email(email):
    '''
    '''
    try:
        is_exists = User.objects.filter(email=email).exists()
        return {'is_exists':is_exists}
    except Exception as e:
        pass
