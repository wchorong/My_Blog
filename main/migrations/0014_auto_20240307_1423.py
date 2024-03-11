# Generated by Django 3.2.22 on 2024-03-07 05:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_sub_blog_code_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_blog',
            name='code_set',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sub_blog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, default=1, verbose_name='내용'),
            preserve_default=False,
        ),
    ]
