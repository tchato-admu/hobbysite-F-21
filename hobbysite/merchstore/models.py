from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['name']


class Product(models.Model):
    status_choices = [
        ('AVAILABLE', 'Available'),
        ('ON_SALE', 'On Sale'),
        ('OUT_OF_STOCK', 'Out of Stock')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default='1')
    status = models.CharField(max_length=12, choices=status_choices, default='AVAILABLE')
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='product',
        null=True
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('merchstore:product-detail', args=[self.pk])


    def update_product_url(self):
        return reverse('merchstore:product-update', args=[self.pk]) 
    

    class Meta:
        ordering = ['name']


class Transaction(models.Model):
    status_choices = [
        ('ON_CART', 'On Cart'),
        ('TO_PAY', 'To Pay'),
        ('TO_SHIP', 'To Ship'),
        ('TO_RECEIVE', 'To Receive'),
        ('DELIVERED', 'Delivered')
    ]

    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='transactions',
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='transactions'
    )
    amount = models.PositiveBigIntegerField()
    status = models.CharField(max_length=10, choices=status_choices)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
