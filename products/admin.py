from django.contrib import admin

from products.models import CategoryModel, ProductModel, CartModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-pk']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product_title', 'product_price', 'product_created_at']
    search_fields = ['product_title']
    list_filter = ['product_created_at']
    ordering = ['-pk']


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_product', 'user_product_quantity', 'user_add_date']
    search_fields = ['user_id', 'user_product']
    list_filter = ['user_add_date']
    ordering = ['-pk']
