from django.contrib import admin

from .models import Thread, ThreadCategory, Comment

admin.site.register(Thread)
admin.site.register(ThreadCategory)
admin.site.register(Comment)