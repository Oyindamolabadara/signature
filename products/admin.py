from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'category',
        'colour',
        'stock_level',
        'price',
        'rating',
        'image',
        'chain_width',
        'chain_length',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)