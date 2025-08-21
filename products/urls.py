from django.urls import path

from .views import (
    ProductCategoryCreateView,
    ProductCategoryDestroyView,
    ProductCategoryDetailView,
    ProductCategoryListView,
    ProductCategoryUpdateView,
    ProductCreateView,
    ProductDestroyView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    ProductVariantCreateView,
    ProductVariantDestroyView,
    ProductVariantDetailView,
    ProductVariantListView,
    ProductVariantUpdateView,
)

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDestroyView.as_view(), name="product-delete"
    ),
    path("categories/", ProductCategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:pk>/",
        ProductCategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "categories/create/",
        ProductCategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "categories/<int:pk>/update/",
        ProductCategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        ProductCategoryDestroyView.as_view(),
        name="category-delete",
    ),
    path("variants/", ProductVariantListView.as_view(), name="variant-list"),
    path(
        "variants/<int:pk>/", ProductVariantDetailView.as_view(), name="variant-detail"
    ),
    path("variants/create/", ProductVariantCreateView.as_view(), name="variant-create"),
    path(
        "variants/<int:pk>/update/",
        ProductVariantUpdateView.as_view(),
        name="variant-update",
    ),
    path(
        "variants/<int:pk>/delete/",
        ProductVariantDestroyView.as_view(),
        name="variant-delete",
    ),
]
