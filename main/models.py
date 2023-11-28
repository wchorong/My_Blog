from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, number, password=None, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(number, password=None, **other_fields)

    def create_user(self, number, password=None, email=None, **other_fields):

        if not number:
            raise ValueError(_('You must provide an email address'))

        user = self.model(number=number, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    number = models.CharField(max_length=20, unique=True)
    # 다른 필드들을 추가할 수 있습니다.

    objects = CustomAccountManager()

    USERNAME_FIELD = 'number'


    def __str__(self):
        return self.number

class BaseModel(models.Model):
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    CATEGORY_TITLE = (
        ('Stack', 'Stack'),
        ('Language', 'Language'),
        ('CSS', 'CSS'),
        ('Basic', 'Basic'),)
    category_title = models.CharField(verbose_name='category', choices=CATEGORY_TITLE, blank=True, max_length=10)

class Blog(BaseModel):
    title = models.CharField(max_length=50)
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Sub_blog(BaseModel):
    subtitle = models.CharField(max_length=100)
    content = RichTextUploadingField()
    code_set = models.TextField()
    img = models.ImageField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
