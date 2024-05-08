from django.urls import path

from .views import product_list, product_detail, product_create, product_update, transactions_cart, transactions_list


urlpatterns = [
    path('merchstore/items', product_list, name = 'list'),
    path('merchstore/item/<int:pk>', product_detail, name = 'product-detail'),
    path('merchstore/item/add', product_create, name = 'product-create'),   
    path('merchstore/item/<int:pk>/edit', product_update, name = 'product-update'),    
    path('merchstore/cart', transactions_cart, name = 'cart'),
    path('merchstore/transactions', transactions_list, name = 'transaction-list')
]

app_name = "merchstore"