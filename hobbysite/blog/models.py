from datetime import datetime
from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta: 
        ordering = ['name']
        verbose_name = 'Category'  
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('blog:article_list')
    
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null = True, related_name='blogArticleAuthor')
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null = True, related_name='blogArticleCategory')
    entry = models.TextField()
    header_image = models.ImageField(upload_to='images/', null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.pk])
    
class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='blogCommentsAuthor')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='blogCommentsArticle')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'
