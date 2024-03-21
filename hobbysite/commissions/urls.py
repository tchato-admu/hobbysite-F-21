from django.urls import path

from .views import commissions_detail, commissions_list

urlpatterns = [
    path("list", commissions_list, name="commissions_list"),
    path("detail/<int:pk>", commissions_detail, name="commissions_detail"),
]

app_name = "commissions"