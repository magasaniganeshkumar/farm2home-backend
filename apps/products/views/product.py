from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.products.choices import CatalogStatus
from apps.products.models import Product
from apps.products.serializers import (
    ProductDetailSerializer,
    ProductListSerializer,
)


@extend_schema(tags=["Products"])
class ProductListView(generics.ListAPIView):
    """
    Public product catalog.
    """

    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    queryset = (
        Product.objects.select_related("category")
        .filter(
            status=CatalogStatus.ACTIVE,
        )
        .order_by("name")
    )


@extend_schema(tags=["Products"])
class ProductDetailView(generics.RetrieveAPIView):
    """
    Public product details.
    """

    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]

    queryset = (
        Product.objects.select_related("category")
        .filter(
            status=CatalogStatus.ACTIVE,
        )
    )