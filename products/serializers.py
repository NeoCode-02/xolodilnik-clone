from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Product, ProductCategory, ProductVariant


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")

    def validate_name(self, value):
        if self.instance and self.instance.name.lower() == value.lower():
            return value
        if ProductCategory.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                _("A category with this name already exists.")
            )
        return value


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(_("Stock cannot be negative."))
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(_("Price must be greater than zero."))
        return value


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(),
        source="category",
        write_only=True,
        required=True,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "image",
            "category",
            "category_id",
            "is_featured",
            "variants",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(_("Price must be greater than zero."))
        return value
