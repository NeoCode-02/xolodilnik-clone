from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price")
    )
    image = models.ImageField(upload_to="products", verbose_name=_("Image"))
    category = models.ForeignKey(
        "products.ProductCategory",
        on_delete=models.RESTRICT,
        related_name="products",
        verbose_name=_("Category"),
    )
    is_featured = models.BooleanField(default=False, verbose_name=_("Is Featured"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductVariant(BaseModel):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.RESTRICT,
        related_name="variants",
        verbose_name=_("Product"),
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price")
    )
    color = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Color")
    )
    size = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Size")
    )
    stock = models.PositiveIntegerField(verbose_name=_("Stock"))

    def __str__(self):
        variant_info = [self.product.name]
        if self.color:
            variant_info.append(self.color)
        if self.size:
            variant_info.append(self.size)
        return " - ".join(variant_info)

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")


class ProductCategory(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name=_("Name"))
    description = models.CharField(
        max_length=500, blank=True, verbose_name=_("Description")
    )
    image = models.ImageField(
        upload_to="categories/", blank=True, null=True, verbose_name=_("Image")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    sort_order = models.PositiveSmallIntegerField(
        default=0, verbose_name=_("Sort Order")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name
