from django.urls import path

from .views import commission_detail, commission_list

urlpatterns = [
    path("list", commission_list, name="commission_list"),
    path("detail/<int:pk>", commission_detail, name="commission_detail"),
]

app_name = "commissions"