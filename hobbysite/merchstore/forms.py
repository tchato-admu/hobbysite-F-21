from django import forms
from .models import Transaction, Product, ProductType
from user_management.models import Profile


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']


class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(label='Product Name')
    product_type = forms.ModelChoiceField(queryset=ProductType.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label='Product Type')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'status', 'product_type']
        widgets = {
            'status': forms.Select(choices=Product.status_choices),
        }


class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Product Name')
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'status', 'product_type']
        widgets = {
            'status': forms.Select(choices=Product.status_choices),
        }
