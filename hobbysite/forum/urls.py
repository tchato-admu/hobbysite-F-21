from django.urls import path
from .views import PostListView, PostDetailView


app_name = 'forum'

urlpatterns = [
    path('threads/', PostListView.as_view(), name = 'post_list'),
    path('thread/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
]