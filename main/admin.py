from django.contrib import admin
from main.models import Blog
from main.models import Sub_blog, Category, Blog

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sub_blog,AuthorAdmin)

class AuthorAdmin2(admin.ModelAdmin):
    pass

admin.site.register(Category,AuthorAdmin2)
class AuthorAdmin3(admin.ModelAdmin):
    pass


admin.site.register(Blog, AuthorAdmin2)