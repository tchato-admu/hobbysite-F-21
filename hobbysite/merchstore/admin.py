from django.contrib import admin

from .models import Product, ProductType

    
class ProductAdmin(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductAdmin,]


admin.site.register(ProductType, ProductTypeAdmin)