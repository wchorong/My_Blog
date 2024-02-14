from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Category(models.Model): # 상위 카테고리
    category_name = models.CharField(max_length=50)
    CATEGORY_TITLE = (
        ('Stack', 'Stack'),
        ('Language', 'Language'),
        ('CSS', 'CSS'),
        ('Basic', 'Basic'),)
    category_title = models.CharField(verbose_name='category', choices=CATEGORY_TITLE, blank=True, max_length=10)

class Blog(BaseModel): # 하위 카테고리
    title = models.CharField(max_length=50)
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Sub_blog(BaseModel): # 하위 카테고리 내의 글
    subtitle = models.CharField(max_length=100)
    content = RichTextField('내용', blank=True, null=True)
    code_set = models.TextField('Code Pen')
    img = models.ImageField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
