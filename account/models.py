from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, password, **other_fields)

    def create_user(self, username, password, **other_fields):

        if not username:
            raise ValueError(_('You must provide an username address'))

        user = self.model(username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    start = models.DateTimeField(default=timezone.now)  # 생성 날짜
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)



    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username