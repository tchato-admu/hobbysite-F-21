from django.urls import path
from .views import article_list, ArticleDetailView

urlpatterns = [
    path('articles', article_list, name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail')
]

app_name = 'wiki'