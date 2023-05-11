from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add-blog',views.add_blog,name='add_blog'),
    path('my-blog-list',views.my_blog_list,name='my_blog_list'),
    path('edit-blog/<str:blog_id>/',views.edit_blog,name='edit_blog'),
    path('delete-blog/<str:blog_id>/',views.delete_blog,name='delete_blog'),
    path('blog/<str:id>/',views.blog,name='blog'),
]