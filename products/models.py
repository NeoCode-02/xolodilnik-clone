from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products")
    category = models.ForeignKey(
        "products.ProductCategory", on_delete=models.RESTRICT, related_name="products"
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductVariant(BaseModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.RESTRICT, related_name="variants"
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")


class ProductCategory(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name
