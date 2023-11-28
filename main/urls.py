from django.urls import path
from .views import Main, Test, Blog, Blog_post, Blog_list

app_name = 'main'

urlpatterns = [
    path('test/', Test.as_view(), name='Test'),
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/post', Blog_post.as_view(), name='blog_post'),
    path('blog/list', Blog_list.as_view(), name='blog_list'),

]