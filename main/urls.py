from django.urls import path
from .views import Blog, Blog_post, Blog_list

app_name = 'main'

urlpatterns = [
    path('post', Blog_post.as_view(), name='blog_post'),
    path('list', Blog_list.as_view(), name='blog_list'),
    path('', Blog.as_view(), name='blog'),

]