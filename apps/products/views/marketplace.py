from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.products.choices import SupplierProductStatus
from apps.products.models import SupplierProduct
from apps.products.serializers import (
    MarketplaceProductListSerializer,
)


@extend_schema(tags=["Marketplace"])
class MarketplaceProductListView(generics.ListAPIView):
    """
    Public marketplace products.
    """

    serializer_class = MarketplaceProductListSerializer
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
        .order_by("-created_at")
    )