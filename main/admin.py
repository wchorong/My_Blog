from django.contrib import admin
from main.models import Blog
from main.models import Sub_blog

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sub_blog, AuthorAdmin)