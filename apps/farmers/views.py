from rest_framework import generics, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Farmer, FarmerStatus
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)



from .models import Farmer, FarmingType
from .serializers import (
    SupplierApplicationSerializer,
    FarmerUpdateSerializer,
    FarmerListSerializer,
    FarmerDetailSerializer,
)
from .services import FarmerService


@extend_schema(tags=["Suppliers"])
class SupplierApplicationView(generics.GenericAPIView):
    """
    Customer applies to become a supplier.
    """

    serializer_class = SupplierApplicationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            farmer = FarmerService.apply_supplier(
                request.user,
                serializer.validated_data,
            )
        except ValueError as exc:
            return Response(
                {"message": str(exc)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": "Supplier application submitted successfully.",
                "status": farmer.verification_status,
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=["Suppliers"])
class FarmerListView(generics.ListAPIView):
    """
    List all suppliers.
    Admin only.
    """

    permission_classes = [IsAdminUser]

    queryset = Farmer.objects.select_related("user")

    serializer_class = FarmerListSerializer


@extend_schema(tags=["Suppliers"])
class MySupplierProfileView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update the logged-in supplier profile.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return self.request.user.farmer_profile
        except Farmer.DoesNotExist:
            raise NotFound(
                "You have not applied to become a supplier yet."
            )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FarmerDetailSerializer
        return FarmerUpdateSerializer

    def perform_update(self, serializer):
        farmer = FarmerService.update_farmer(
            self.get_object(),
            serializer.validated_data,
        )
        serializer.instance = farmer


@extend_schema(tags=["Suppliers"])
class SupplierStatusView(generics.GenericAPIView):
    """
    Get supplier application status.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            farmer = request.user.farmer_profile
        except Farmer.DoesNotExist:
            return Response(
                {
                    "message": "You have not applied to become a supplier yet."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        messages = {
            FarmerStatus.PENDING: "Your supplier application is under review.",
            FarmerStatus.VERIFIED: "Your supplier account has been verified.",
            FarmerStatus.REJECTED: "Your supplier application was rejected.",
        }

        return Response(
            {
                "status": farmer.verification_status,
                "message": messages.get(
                    farmer.verification_status,
                    "Unknown status.",
                ),
            }
        )


@extend_schema(tags=["Admin - Suppliers"])
class AdminSupplierListView(generics.ListAPIView):
    """
    Admin: List all supplier applications.
    """

    permission_classes = [IsAdminUser]

    queryset = Farmer.objects.select_related("user")

    serializer_class = FarmerListSerializer


@extend_schema(tags=["Admin - Suppliers"])
class AdminSupplierDetailView(generics.RetrieveDestroyAPIView):
    """
    Admin: Retrieve supplier details.
    """

    permission_classes = [IsAdminUser]

    queryset = Farmer.objects.select_related("user")

    serializer_class = FarmerDetailSerializer

    def perform_destroy(self, instance):
        instance.soft_delete()


@extend_schema(
    tags=["Admin - Suppliers"],
    request=None,
)
class AdminVerifySupplierView(generics.GenericAPIView):
    """
    Admin: Verify supplier.
    """

    permission_classes = [IsAdminUser]
    queryset = Farmer.objects.select_related("user")

    def patch(self, request, *args, **kwargs):
        farmer = self.get_object()

        FarmerService.verify_farmer(farmer)

        return Response(
            {
                "message": "Supplier verified successfully."
            },
            status=status.HTTP_200_OK,
        )


@extend_schema(
    tags=["Admin - Suppliers"],
    request=None,
)
class AdminRejectSupplierView(generics.GenericAPIView):
    """
    Admin: Reject supplier.
    """

    permission_classes = [IsAdminUser]
    queryset = Farmer.objects.select_related("user")

    def patch(self, request, *args, **kwargs):
        farmer = self.get_object()

        FarmerService.reject_farmer(farmer)

        return Response(
            {
                "message": "Supplier rejected successfully."
            },
            status=status.HTTP_200_OK,
        )

