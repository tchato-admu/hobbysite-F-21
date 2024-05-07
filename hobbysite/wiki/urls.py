from django.urls import path
from .views import article_list, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('articles', article_list, name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/add', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name='article_update'),
]

app_name = 'wiki'