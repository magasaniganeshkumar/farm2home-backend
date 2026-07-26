from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.products.models import SupplierProduct
from apps.products.serializers import (
    SupplierProductCreateSerializer,
    SupplierProductDetailSerializer,
    SupplierProductListSerializer,
    SupplierProductUpdateSerializer,
)
from apps.products.services import SupplierProductService


@extend_schema(tags=["Supplier Products"])
class SupplierProductListCreateView(generics.ListCreateAPIView):
    """
    List and create supplier products.
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            SupplierProduct.objects.select_related(
                "product",
                "product__category",
                "farmer",
            )
            .filter(farmer__user=self.request.user)
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SupplierProductCreateSerializer
        return SupplierProductListSerializer

    def perform_create(self, serializer):
        SupplierProductService.create_listing(
            farmer=self.request.user.farmer,
            validated_data=serializer.validated_data,
        )


@extend_schema(tags=["Supplier Products"])
class SupplierProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete a supplier product.
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            SupplierProduct.objects.select_related(
                "product",
                "product__category",
                "farmer",
            )
            .filter(farmer__user=self.request.user)
        )

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return SupplierProductUpdateSerializer
        return SupplierProductDetailSerializer

    def perform_update(self, serializer):
        SupplierProductService.update_listing(
            listing=self.get_object(),
            validated_data=serializer.validated_data,
        )