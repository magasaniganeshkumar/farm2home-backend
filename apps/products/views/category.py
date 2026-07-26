from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.products.models import Category
from apps.products.serializers import (
    CategoryDetailSerializer,
    CategoryListSerializer,
)


@extend_schema(tags=["Categories"])
class CategoryListView(generics.ListAPIView):
    """
    Public category list.
    """

    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]

    queryset = (
        Category.objects.filter(
            is_active=True,
            is_visible=True,
        )
        .order_by("display_order", "name")
    )


@extend_schema(tags=["Categories"])
class CategoryDetailView(generics.RetrieveAPIView):
    """
    Public category details.
    """

    serializer_class = CategoryDetailSerializer
    permission_classes = [AllowAny]

    queryset = Category.objects.filter(
        is_active=True,
        is_visible=True,
    )