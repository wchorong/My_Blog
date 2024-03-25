from rest_framework import serializers
from .models import Sub_blog, Blog, Category

class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_blog
        fields = '__all__'

    def create(self, validated_data):
        blog_set = Blog.objects.get(id=self.context.get('pk'))
        bool = Sub_blog.objects.create(subtitle=validated_data['subtitle'],
                                    content=validated_data['content'],
                                   code_set=validated_data['code_set'],
                                    blog=blog_set,
                                   )
        return bool

    def update(self, instance, validated_data):
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.content = validated_data.get('content', instance.content)
        instance.code_set = validated_data.get('code_set', instance.code_set)
        instance.blog = validated_data.get('blog', instance.blog)
        instance.save()
        return instance

class Title_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def validate(self, data):
        return data
    def create(self, validated_data):
        Cat = self.context.get('cate')
        cat_model = Category.objects.get(category_name=Cat)
        bool = Blog.objects.create(title=validated_data['title'],
                                   sub_title=validated_data['sub_title'],
                                   img=validated_data['img'],
                                   category=cat_model,
                                   )
        return bool

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.sub_title = validated_data.get('sub_title', instance.sub_title)
        img = validated_data.pop('img', None)
        if img:
            instance.img = img
        instance.save()
        return instance


class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("category_name", "category_title")

    def create(self, validated_data):
        cate = self.context.get('cate')
        bool = Category.objects.create(category_name=validated_data['category_name'],
                                       category_title=cate,
                                       )
        return bool

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.category_title = validated_data.get('category_title', instance.category_title)
        instance.save()
        return instance