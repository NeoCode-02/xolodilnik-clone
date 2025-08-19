from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TransactionStatus(TextChoices):
    PENDING = "pending", _("Pending")
    PAID = "paid", _("Paid")
    CANCELLED = "cancelled", _("Cancelled")
    FAILED = "failed", _("Failed")


class OrderStatus(TextChoices):
    PENDING = "pending", _("Pending")
    PAID = "paid", _("Paid")
    CANCELLED = "cancelled", _("Cancelled")
    FAILED = "failed", _("Failed")


class DiscountTypeChoices(TextChoices):
    PERCENTAGE = "percentage", _("Percentage")
    FIXED = "fixed", _("Fixed")
