from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Product, ProductType, Transaction
from user_management.models import Profile
from .forms import TransactionForm, ProductCreateForm, ProductUpdateForm


def product_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        product_types = ProductType.objects.all()
        ctx = {
            'product_types': product_types,
            'all_products': Product.objects.all(),
            'user_products': Product.objects.filter(owner=profile),
            'other_products': Product.objects.exclude(owner=profile)
        }
    else:
        product_types = ProductType.objects.all()
        ctx = {
            'product_types': product_types,
            'all_products': Product.objects.all(),
        }
    return render(request, 'merchstore/product_list.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                transaction = form.save(commit=False)
                transaction.amount = form.cleaned_data.get('amount')                  
                transaction.product = product
                transaction.created_on = timezone.now()
                if product.stock >= transaction.amount:
                    product.stock -= transaction.amount
                    if product.stock == 0:
                        product.status = Product.status_choices[2][1]
                    product.save()
                transaction.status = Transaction.status_choices[0][1]
                transaction.buyer = request.user.profile
                transaction.save()
                return redirect(reverse('merchstore:cart'))
            else:
                return redirect(reverse('user_management:user_registration'))
    ctx = {
        'product': product,
        'form': form
    }
    return render(request, 'merchstore/product_detail.html', ctx)


@login_required
def product_create(request):
    owner = request.user.profile
    form = ProductCreateForm()
    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.price = form.cleaned_data.get('price')
            product.stock = form.cleaned_data.get('stock')
            product.product_type = form.cleaned_data.get('product_type')
            product.status = form.cleaned_data.get('status')
            if product.stock == 0:
                product.status = Product.status_choices[2][1]
            elif product.stock > 0 and product.status == Product.status_choices[2][0]:
                product.status = Product.status_choices[0][1]
            product.owner = owner
            product.save()
            return redirect(reverse('merchstore:list'))
    ctx = {
        'owner': owner,
        'form': form
    }
    return render(request, 'merchstore/product_create.html', ctx)


@login_required
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    owner = request.user.profile
    form = ProductUpdateForm()
    if request.method == "POST":
        form = ProductUpdateForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.price = form.cleaned_data.get('price')
            product.product_type = form.cleaned_data.get('product_type')
            product.owner = owner
            product.stock = form.cleaned_data.get('stock')

            if product.stock == 0:
                product.status = Product.status_choices[2][1]
            else:
                product.status = form.cleaned_data.get('status')
            product.save()
            return redirect(reverse('merchstore:list'))
    ctx = {
        'owner': owner,
        'form': form
    }
    return render(request, 'merchstore/product_update.html', ctx)


@login_required
def transactions_cart(request):
    user = Profile.objects.get(user=request.user)
    user_transactions = Transaction.objects.filter(buyer=user)
    transactions_by_owner = {}
    for transaction in user_transactions:
        owner = transaction.product.owner
        if owner not in transactions_by_owner:
            transactions_by_owner[owner] = []
        transactions_by_owner[owner].append(transaction)  
    ctx = {
        'transactions_by_owner': transactions_by_owner,
    }
    return render(request, 'merchstore/transactions_cart.html', ctx)


@login_required
def transactions_list(request):
    user = Profile.objects.get(user=request.user)
    user_products = Transaction.objects.filter(product__owner=user)
    transactions_by_buyers = {}

    for transaction in user_products:
        buyer = transaction.buyer
        if buyer not in transactions_by_buyers:
            transactions_by_buyers[buyer] = []
        transactions_by_buyers[buyer].append(transaction)

    ctx = {
        'transactions_by_buyers': transactions_by_buyers,
    }
    return render(request, 'merchstore/transactions_list.html', ctx)