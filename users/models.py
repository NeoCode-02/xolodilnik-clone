from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    phone_number = models.CharField(
        _("Phone Number"), max_length=20, null=True, blank=True
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profession = models.ForeignKey(
        "users.Profession",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="users",
    )
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    favourites = models.ManyToManyField(
        "products.ProductVariant",
        through="UserFavorites",
        related_name="favourite_users",
    )
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email


class Profession(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Profession")
        verbose_name_plural = _("Professions")


class Cart(BaseModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class CartItem(BaseModel):
    cart = models.ForeignKey(
        "users.Cart", on_delete=models.CASCADE, related_name="cart_items"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="cart_items"
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} - {self.quantity}"

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")


class UserFavorites(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product_variant = models.ForeignKey(
        "products.ProductVariant", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.product_variant}"

    class Meta:
        verbose_name = _("User Favorite")
        verbose_name_plural = _("User Favorites")
        unique_together = ("user", "product_variant")


class UserFeedback(BaseModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="feedbacks"
    )
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user} - {self.message}"

    class Meta:
        verbose_name = _("User Feedback")
        verbose_name_plural = _("User Feedbacks")
