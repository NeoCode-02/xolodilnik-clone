from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Product, ProductCategory, ProductVariant


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ["id", "name", "category", "is_featured", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "category__name"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "name", "category", "is_featured", "created_at", "updated_at"]
    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "price",
                    "image",
                    "category",
                    "is_featured",
                )
            },
        ),
        (
            _("Uzbek"),
            {
                "fields": (
                    "name_uz",
                    "description_uz",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "name_en",
                    "description_en",
                )
            },
        ),
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                    "description_ru",
                )
            },
        ),
    )

@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ["id", "name", "is_active", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "name", "is_active", "created_at", "updated_at"]

    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "image",
                    "is_active",
                    "sort_order",
                )
            },
        ),
        (
            _("Uzbek"),
            {
                "fields": (
                    "name_uz",
                    "description_uz",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "name_en",
                    "description_en",
                )
            },
        ),
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                    "description_ru",
                )
            },
        ),
    )

@admin.register(ProductVariant)
class ProductVariantAdmin(TranslationAdmin):
    list_display = [
        "id",
        "product",
        "name",
        "color",
        "size",
        "price",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["id", "product", "name"]
    search_fields = ["product__name", "name", "color", "size"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "product", "name", "color", "size", "created_at", "updated_at"]

    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "product",
                    "price",
                    "stock",
                )
            },
        ),
        (
            _("Uzbek"),
            {
                "fields": (
                    "name_uz",
                    "color_uz",
                    "size_uz",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "name_en",
                    "color_en",
                    "size_en",
                )
            },
        ),
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                    "color_ru",
                    "size_ru",
                )
            },
        ),
    )