from django.db import models


class ArticleCategory(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()

    class Meta: 
        ordering = ['Name']

    def __str__(self):
        return self.Name 
    
class Article(models.Model):
    Title = models.CharField(max_length=255)
    Category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null = True)
    Entry = models.TextField()
    Created_on = models.DateTimeField(auto_now_add=True)
    Updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-Created_on']

    def __str__(self):
        return self.Title
