from django.urls import path
from .views import UserUpdateView


app_name = 'user_managment'

urlpatterns = [
    path('', UserUpdateView.as_view(), name='user_detail')
]