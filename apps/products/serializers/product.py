from rest_framework import serializers

from apps.products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "product_code",
            "name",
            "slug",
            "category",
            "category_name",
            "default_unit",
            "status",
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    category_code = serializers.CharField(
        source="category.code",
        read_only=True,
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "product_code",
            "name",
            "slug",
            "description",
            "category",
            "category_name",
            "category_code",
            "default_unit",
            "product_type",
            "season",
            "storage_type",
            "status",
            "is_featured",
        )