from django.urls import path 
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView


app_name = 'blog'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name = 'article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('article/create/', ArticleCreateView.as_view(), name = 'article_create'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name = 'article_update'),
]