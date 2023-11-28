from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class Main(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, reqeust):
        return Response(status=status.HTTP_200_OK, template_name='index.html')

class Test(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, reqeust):
        return Response(status=status.HTTP_200_OK, template_name='test.html')

class Blog(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, reqeust):
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_main.html')

class Blog_post(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, reqeust):
        return Response(status=status.HTTP_200_OK, template_name='blog/blog.html')

class Blog_list(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, reqeust):
        return Response(status=status.HTTP_200_OK, template_name='blog/blog_list.html')
