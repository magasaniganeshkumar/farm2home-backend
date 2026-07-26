from rest_framework import serializers

from apps.products.models import SupplierProduct


class SupplierProductCreateSerializer(serializers.ModelSerializer):
    """
    Supplier creates a product listing.
    """

    class Meta:
        model = SupplierProduct
        fields = (
            "product",
            "selling_price",
            "discount_price",
            "available_quantity",
            "minimum_order_quantity",
            "estimated_delivery_days",
            "pickup_available",
            "home_delivery",
            "is_organic",
            "is_certified",
            "grade",
            "description",
            "notes",
            "harvest_date",
            "available_from",
            "available_until",
        )

    def validate(self, attrs):
        selling_price = attrs.get("selling_price")
        discount_price = attrs.get("discount_price")

        if (
            discount_price is not None
            and discount_price > selling_price
        ):
            raise serializers.ValidationError(
                {
                    "discount_price": (
                        "Discount price cannot be greater than selling price."
                    )
                }
            )

        return attrs


class SupplierProductUpdateSerializer(
    SupplierProductCreateSerializer
):
    """
    Supplier updates a product listing.
    """

    pass


class SupplierProductListSerializer(serializers.ModelSerializer):
    """
    Supplier listing summary.
    """

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    category = serializers.CharField(
        source="product.category.name",
        read_only=True,
    )

    class Meta:
        model = SupplierProduct
        fields = (
            "id",
            "listing_code",
            "product_name",
            "category",
            "selling_price",
            "available_quantity",
            "status",
            "is_visible",
        )


class SupplierProductDetailSerializer(serializers.ModelSerializer):
    """
    Supplier listing details.
    """

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    category = serializers.CharField(
        source="product.category.name",
        read_only=True,
    )

    class Meta:
        model = SupplierProduct
        fields = "__all__"