from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from apps.products.filters import MarketplaceProductFilter

from apps.products.choices import SupplierProductStatus
from apps.products.models import SupplierProduct
from apps.products.serializers import (
    MarketplaceProductDetailSerializer,
    MarketplaceProductListSerializer,
)


@extend_schema(tags=["Marketplace"])
class MarketplaceProductListView(generics.ListAPIView):
    """
    Public marketplace products.
    """

    serializer_class = MarketplaceProductListSerializer
    permission_classes = [AllowAny]

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    filterset_class = MarketplaceProductFilter

    search_fields = [
        "product__name",
        "product__category__name",
        "farmer__user__full_name",
    ]

    ordering_fields = [
        "selling_price",
        "created_at",
        "available_quantity",
    ]

    ordering = [
        "-created_at",
    ]

    queryset = (
        SupplierProduct.objects.select_related(
            "product",
            "product__category",
            "farmer",
            "farmer__user",
        )
        .filter(
            status=SupplierProductStatus.LIVE,
            is_visible=True,
        )
    )

@extend_schema(tags=["Marketplace"])
class MarketplaceProductDetailView(generics.RetrieveAPIView):
    """
    Public marketplace product details.
    """

    serializer_class = MarketplaceProductDetailSerializer
    permission_classes = [AllowAny]

    queryset = (
        SupplierProduct.objects.select_related(
            "product",
            "product__category",
            "farmer",
            "farmer__user",
        )
        .filter(
            status=SupplierProductStatus.LIVE,
            is_visible=True,
        )
    )