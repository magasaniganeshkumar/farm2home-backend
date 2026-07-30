import django_filters

from apps.products.models import SupplierProduct


class MarketplaceProductFilter(django_filters.FilterSet):
    """
    Marketplace product filters.
    """

    category = django_filters.UUIDFilter(
        field_name="product__category__id"
    )

    is_organic = django_filters.BooleanFilter()

    is_certified = django_filters.BooleanFilter()

    min_price = django_filters.NumberFilter(
        field_name="selling_price",
        lookup_expr="gte",
    )

    max_price = django_filters.NumberFilter(
        field_name="selling_price",
        lookup_expr="lte",
    )

    class Meta:
        model = SupplierProduct
        fields = [
            "category",
            "is_organic",
            "is_certified",
        ]