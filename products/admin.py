from django.contrib import admin

from products.models import Product, ProductVariant, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "is_featured", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "category__name"]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]    


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "name", "color", "size", "price", "created_at", "updated_at"]
    list_display_links = ["id", "product", "name"]
    search_fields = ["product__name", "name", "color", "size"]