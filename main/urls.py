from django.urls import path, include
from .views import Blog, Blog_post, Blog_list, Blog_crud, Main_category_make, Blog_list_crud
from django.conf.urls.static import static
from django.conf import settings
app_name = 'main'

urlpatterns = [
    path('post', Blog_post.as_view(), name='blog_post'),
    path('cate_set', Main_category_make.as_view(), name='main_category_make'),
    path('list_crud', Blog_list_crud.as_view(), name='blog_list_crud'),
    path('list/<str:cate>', Blog_list.as_view(), name='blog_list'),
    path('crud', Blog_crud.as_view(), name='blog_crud'),
    path('', Blog.as_view(), name='blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
