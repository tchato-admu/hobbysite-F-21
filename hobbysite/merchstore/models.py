from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
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


    class Meta:
        ordering = ['name']