from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('sign-in',views.sign_in,name='sign_in'),
    path('profile',views.profile,name='profile'),
    path('sign-out',views.sign_out,name='sign_out'),
    path('ajax/check-username/',views.check_username,name='check_username'),
    path('ajax/check-email/',views.check_email,name='check_email'),
]