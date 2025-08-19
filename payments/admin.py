from django.contrib import admin

from payments.models import (
    Discount,
    Order,
    OrderItem,
    ProductDiscount,
    Promocode,
    PromocodeUsage,
    Provider,
    Transaction,
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user__email",
        "total_amount",
        "status",
        "ordered_at",
        "purchased_at",
    )
    list_display_links = ("id", "user__email")
    search_fields = ("user__email", "user__first_name", "user__last_name")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product__name", "quantity", "price")
    list_display_links = ("id", "order", "product__name")
    search_fields = (
        "order__user__email",
        "order__user__first_name",
        "order__user__last_name",
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "provider",
        "status",
        "amount",
        "paid_at",
        "cancelled_at",
    )
    list_display_links = ("id", "order", "provider")
    search_fields = (
        "order__user__email",
        "order__user__first_name",
        "order__user__last_name",
    )


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")
    list_filter = ("name",)
    ordering = ["name"]


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "description",
        "type",
        "value",
        "min_amount",
        "usage_limit",
    )
    search_fields = ("code", "description")
    list_display_links = ("id", "code")
    list_filter = ("type",)
    ordering = ["code"]


@admin.register(PromocodeUsage)
class PromocodeUsageAdmin(admin.ModelAdmin):
    list_display = ("id", "promocode_id__code", "used_at")
    search_fields = ("promocode_id__code", "promocode__description")
    list_display_links = ("id", "promocode_id__code")


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "discount_type", "value")
    search_fields = ("name", "description")
    list_display_links = ("id", "name")
    list_filter = ("discount_type",)
    ordering = ["name"]


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "discount", "valid_from", "valid_until")
    search_fields = ("product__name", "discount__name")
    list_display_links = ("id", "product", "discount")
    ordering = ["product"]
