from django.urls import path

from .views import commissions_detail, commissions_list, commissions_edit, commissions_create

urlpatterns = [
    path("list", commissions_list, name="commissions_list"),
    path("detail/<int:pk>", commissions_detail, name="commissions_detail"),
    path("add", commissions_create, name="commissions_add"),
    path("<int:pk>/edit", commissions_edit, name="commissions_edit"),
]

app_name = "commissions"