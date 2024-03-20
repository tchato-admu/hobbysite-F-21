from django.urls import path

from .views import product_list, product_detail

urlpatterns = [
    path('merchstore/items', product_list, name = 'list'),
    path('merchstore/item/<int:pk>', product_detail, name = 'product-detail'),
]

app_name = "merchstore"