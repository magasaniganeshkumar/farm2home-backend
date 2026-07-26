from rest_framework.permissions import BasePermission

from apps.farmers.models import FarmerStatus


class IsFarmer(BasePermission):
    """
    Allows access only to verified farmers.
    """

    message = "Only verified farmers can access this resource."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            farmer = request.user.farmer
        except Exception:
            return False

        return (
            farmer.is_active
            and farmer.verification_status
            == FarmerStatus.VERIFIED
        )