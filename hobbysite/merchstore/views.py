from django.shortcuts import render

from .models import Product, ProductType


def product_list(request):
    product_types = ProductType.objects.all()

    ctx = {
        'product_types': product_types,
        'products': Product.objects.all(),
    }
    return render(request, 'merchstore/product_list.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {
        'product': product,
    }
    return render(request, 'merchstore/product_detail.html', ctx)