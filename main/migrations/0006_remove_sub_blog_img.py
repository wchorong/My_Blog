# Generated by Django 3.2.22 on 2024-02-20 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_blog_sub_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_blog',
            name='img',
        ),
    ]