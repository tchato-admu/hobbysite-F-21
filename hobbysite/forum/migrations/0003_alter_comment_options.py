# Generated by Django 5.0.3 on 2024-05-07 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_postcategory_threadcategory_thread_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]