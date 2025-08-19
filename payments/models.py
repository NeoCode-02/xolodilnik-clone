from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from payments.choices import DiscountTypeChoices, OrderStatus, TransactionStatus

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    promocode = models.ForeignKey(
        "payments.Promocode",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    total_amount = models.BigIntegerField(null=False, blank=False)
    status = models.CharField(choices=OrderStatus.choices, null=False, blank=False)
    notes = models.CharField(max_length=255, null=True, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    purchased_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order<id={self.id}, price={self.total_price}>"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class OrderItem(BaseModel):
    order = models.ForeignKey(
        "payments.Order",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="items",
    )
    product = models.ForeignKey(
        "products.ProductVariant",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="order_items",
    )
    quantity = models.IntegerField(null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return f"OrderItem<product_id={self.product_id}>"

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")


class Transaction(BaseModel):
    order = models.ForeignKey(
        "payments.Order", on_delete=models.CASCADE, verbose_name=_("order")
    )
    provider = models.ForeignKey(
        "payments.Provider",
        on_delete=models.CASCADE,
        verbose_name=_("Provider"),
        related_name="transactions",
    )
    status = models.CharField(
        max_length=10,
        choices=TransactionStatus.choices,
        default=TransactionStatus.PENDING,
        verbose_name=_("Status"),
    )
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Paid at"))
    cancelled_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Cancelled at")
    )
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name=_("Amount")
    )

    def __str__(self):
        return f"Transaction: {self.id}"

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")


class Provider(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")


class Discount(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    discount_type = models.CharField(choices=DiscountTypeChoices.choices)
    value = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")


class ProductDiscount(BaseModel):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="discounts",
    )
    discount = models.ForeignKey(
        "payments.Discount",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="product_discounts",
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"ProductDiscount<product_id={self.product_id}, discount_id={self.discount_id}>"

    class Meta:
        verbose_name = _("Product Discount")
        verbose_name_plural = _("Product Discounts")


class Promocode(BaseModel):
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    type = models.CharField(choices=DiscountTypeChoices.choices)
    value = models.PositiveIntegerField()
    min_amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    usage_limit = models.PositiveIntegerField(null=True, blank=True)
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_until = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("Promocode")
        verbose_name_plural = _("Promocodes")


class PromocodeUsage(models.Model):
    promocode_id = models.ForeignKey(
        "payments.Promocode", on_delete=models.RESTRICT, related_name="usages"
    )
    used_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PromocodeUsage<promocode_id={self.promocode_id}>"

    class Meta:
        verbose_name = _("Promocode Usage")
        verbose_name_plural = _("Promocode Usages")
