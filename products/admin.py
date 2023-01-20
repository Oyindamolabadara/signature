from django.contrib import admin
from .models import Product, Category, Review

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
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    class to enable admin to  manage user model
    """
    list_display = (
        'product',
        'user',
        'review_time',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)