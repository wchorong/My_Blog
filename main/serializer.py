from rest_framework import serializers
from .models import Sub_blog, Blog, Category

class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_blog
        fields = '__all__'

    def create(self, validated_data):
        blog_set = self.context.get('blog')
        bool = Sub_blog.objects.create(subtitle=validated_data['subtitle'],
                                   content=validated_data['content'],
                                   code_set=validated_data['code_set'],
                                   img=validated_data['img'],
                                    blog=blog_set,
                                   )
        return bool

    def update(self, instance, validated_data):
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.content = validated_data.get('content', instance.content)
        instance.code_set = validated_data.pop('code_set', instance.code_set)
        img = validated_data.pop('title_image', None)
        instance.blog = validated_data.get('blog', instance.blog)

        if img:
            instance.img = img
        instance.save()
        return instance

class Title_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        Cat = self.context.get('cat')
        bool = Blog.objects.create(title=validated_data['title'],
                                   img=validated_data['img'],
                                   category=Cat,
                                   )
        return bool


class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("category_name", "category_title")

    def create(self, validated_data):
        bool = Category.objects.create(category_name=validated_data['category_name'],
                                       category_title=validated_data['category_title'],
                                       )
        return bool

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.category_title = validated_data.get('category_title', instance.category_title)
        instance.save()
        return instance