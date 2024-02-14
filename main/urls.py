from django.urls import path, include
from .views import Blog, Blog_post, Blog_list, Blog_crud
from django.conf.urls.static import static
from django.conf import settings
app_name = 'main'

urlpatterns = [
    path('post', Blog_post.as_view(), name='blog_post'),
    path('list', Blog_list.as_view(), name='blog_list'),
    path('crud', Blog_crud.as_view(), name='blog_crud'),
    path('', Blog.as_view(), name='blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
