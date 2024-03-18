from django.contrib import admin
from .models import ArticleCategory, Article


admin.site.register(ArticleCategory)
admin.site.register(Article)