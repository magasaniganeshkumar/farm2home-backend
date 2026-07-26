from rest_framework import serializers

from apps.products.models import SupplierProduct


class MarketplaceProductListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    category_name = serializers.CharField(
        source="product.category.name",
        read_only=True,
    )

    farmer_name = serializers.CharField(
        source="farmer.user.full_name",
        read_only=True,
    )

    class Meta:
        model = SupplierProduct
        fields = (
            "id",
            "listing_code",
            "product_name",
            "category_name",
            "farmer_name",
            "selling_price",
            "discount_price",
            "available_quantity",
            "estimated_delivery_days",
            "is_organic",
            "is_certified",
            "grade",
            "status",
        )