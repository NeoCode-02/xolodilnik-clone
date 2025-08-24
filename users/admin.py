from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from modeltranslation.admin import TranslationAdmin

from users.models import Profession, Cart, CartItem, UserFavorites, UserFeedback

User = get_user_model()


class CartInline(admin.TabularInline):
    model = Cart
    fields = ["id", "created_at", "updated_at"]
    readonly_fields = ["id", "created_at", "updated_at"]

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "created_at",
    ]
    list_display_links = ["id", "email"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["id"]

    inlines = [CartInline]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


@admin.register(Profession)
class ProfessionAdmin(TranslationAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    list_display_links = ["id", "user"]
    search_fields = ["user__email"]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["id", "cart", "product", "quantity"]
    list_display_links = ["id", "cart", "product"]
    search_fields = ["cart__user__email", "product__name"]

@admin.register(UserFavorites)
class UserFavoritesAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product_variant"]
    list_display_links = ["id", "user", "product_variant"]
    search_fields = ["user__email", "product_variant__name"]

@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "message"]
    list_display_links = ["id", "user", "message"]
    search_fields = ["user__email", "message"]
