from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import Farmer
from .serializers import (
    FarmerCreateSerializer,
    FarmerUpdateSerializer,
    FarmerListSerializer,
    FarmerDetailSerializer,
)
from .services import FarmerService


@extend_schema(tags=["Farmers"])
class FarmerListCreateView(generics.ListCreateAPIView):
    """
    List all farmers or create a new farmer.
    """

    permission_classes = [IsAuthenticated]
    queryset = Farmer.objects.select_related("user")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return FarmerCreateSerializer
        return FarmerListSerializer

    def perform_create(self, serializer):
        farmer = FarmerService.create_farmer(
            serializer.validated_data
        )
        serializer.instance = farmer


@extend_schema(tags=["Farmers"])
class FarmerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a farmer.
    """

    permission_classes = [IsAuthenticated]
    queryset = Farmer.objects.select_related("user")

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return FarmerUpdateSerializer
        return FarmerDetailSerializer

    def perform_update(self, serializer):
        farmer = FarmerService.update_farmer(
            self.get_object(),
            serializer.validated_data,
        )
        serializer.instance = farmer

    def perform_destroy(self, instance):
        instance.soft_delete()