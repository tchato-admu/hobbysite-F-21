from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'user_management.Profile',
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        'ArticleCategory', 
        on_delete=models.SET_NULL,
        null=True
    )
    entry = models.TextField(null=True)
    header_image = models.ImageField(upload_to="images/", null=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('wiki:article_detail', args=[self.pk])
    
    class Meta:
        ordering = ['-createdon']
        
class Comment(models.Model):
    author = models.ForeignKey(
        'user_management.Profile',
        on_delete=models.SET_NULL,
        null=True
    )
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE
    )
    entry = models.TextField(null=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['createdon']
    
    