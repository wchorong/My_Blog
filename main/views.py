from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from main.models import Category, Blog, Sub_blog
from main.serializer import Blog_Serializer, Category_serializer, Title_Serializer
from main.forms import PostAdminForm



class Blog_main(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, reqeust):
        stack, language = Category.objects.filter(category_title="Stack"), Category.objects.filter(category_title="Language")
        css, basic = Category.objects.filter(category_title="CSS"), Category.objects.filter(category_title="Basic")
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_main.html',
                        data={'stack': stack, 'language': language, 'css': css, 'basic': basic})

class Blog_post(APIView): # 블로그
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, reqeust, pk):
        post = Blog.objects.get(id=pk)
        post_box = Sub_blog.objects.filter(blog=post)
        stack, language = Category.objects.filter(category_title="Stack"), Category.objects.filter(
            category_title="Language")
        css, basic = Category.objects.filter(category_title="CSS"), Category.objects.filter(category_title="Basic")
        return Response(status=status.HTTP_200_OK, template_name='blog/blog.html',
                        data={'post_box': post_box, 'post': post, 'blog_id': pk,
                              'stack': stack, 'language': language, 'css': css, 'basic': basic})

class Blog_list(APIView): # 블로그 리스트
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, reqeust, cate):
        blog_cate = Category.objects.get(category_name=cate)
        blog = Blog.objects.filter(category=blog_cate)
        stack, language = Category.objects.filter(category_title="Stack"), Category.objects.filter(category_title="Language")
        css, basic = Category.objects.filter(category_title="CSS"), Category.objects.filter(category_title="Basic")
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_list.html',
                        data={'stack': stack, 'language': language, 'css': css, 'basic': basic, 'blog': blog,
                              'title_name': cate})

class Blog_crud(APIView): # 블로그내 블록 추가
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, reqeust, pk):
        crud_ser = PostAdminForm
        form = Blog_Serializer()
        return Response(status=status.HTTP_200_OK, template_name='blog/CRUD.html', data={'crud': crud_ser, 'pk': pk,
                                                                                         'form': form})

    def post(self, reqeust, pk):
        form = Blog_Serializer(data=reqeust.data, context={'pk': pk})
        if form.is_valid():
            form.save()
            return redirect('main:blog_post', pk=pk)
        else:
            crud_ser = PostAdminForm
            return Response(status=status.HTTP_200_OK, template_name='blog/CRUD.html', data={'crud': crud_ser, 'pk': pk,
                                                                                             'form': form})

class Main_category_make(APIView):  #카테고리 작성 페이지
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, reqeust, cate):
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_main_cate.html', data={'cate': cate})

    def post(self, reqeust, cate):
        form = Category_serializer(data=reqeust.data, context={'cate': cate})
        if form.is_valid():
            form.save()
            return Response(status=status.HTTP_200_OK, template_name='blog/blog_main.html', data={'form': form})
        return redirect('main:main_category_make')

class Blog_list_crud(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, reqeust, cate):
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_sub_cate.html', data={"cate": cate})

    def post(self, request, cate):
        form = Title_Serializer(data=request.data, context={'cate': cate})
        if form.is_valid():
            form.save()
            return redirect('main:mypage')
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_sub_cate.html', data={"cate": cate,
                                                                                                  'form': form})



class My_page(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, reqeust):
        stack, language = Category.objects.filter(category_title="Stack"), Category.objects.filter(
            category_title="Language")
        css, basic = Category.objects.filter(category_title="CSS"), Category.objects.filter(category_title="Basic")

        return Response(status=status.HTTP_200_OK, template_name='blog/my_page.html',
                        data={'stack': stack, 'language': language, 'css': css, 'basic': basic})

class Re_post_list(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, reqeust, pk):
        post = Blog.objects.get(id=pk)
        form = Title_Serializer(instance=post)
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_sub_cate.html', data={'form': form})

    def post(self, reqeust, pk):
        post = Blog.objects.get(id=pk)
        form = Title_Serializer(instance=post, data=reqeust.data)
        if form.is_valid():
            form.save()
            




