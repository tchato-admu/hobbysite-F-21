from django.shortcuts import render

from .models import Product, ProductType


def product_list(request):
    products = Product.objects.all()

    ctx = {
        'products': products,
    }
    return render(request, 'product_list.html', ctx)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {
        'product': product,
    }
    return render(request, 'product_detail.html', ctx)