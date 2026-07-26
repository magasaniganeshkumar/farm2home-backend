from django.utils import timezone

from .models import Farmer, FarmerStatus


class FarmerService:
    """
    Farmer business logic.
    """

    @staticmethod
    def apply_supplier(user, validated_data):
        """
        Customer applies to become a supplier.
        """

        if Farmer.all_objects.filter(user=user).exists():
            raise ValueError(
                "You have already submitted a supplier application."
            )

        return Farmer.objects.create(
            user=user,
            **validated_data,
        )

    @staticmethod
    def update_farmer(farmer, validated_data):
        """
        Update supplier profile.
        """

        for field, value in validated_data.items():
            setattr(farmer, field, value)

        farmer.save()
        return farmer

    @staticmethod
    def verify_farmer(farmer):
        """
        Approve supplier.
        """

        farmer.verification_status = FarmerStatus.VERIFIED
        farmer.verified_at = timezone.now()

        farmer.save(
            update_fields=[
                "verification_status",
                "verified_at",
            ]
        )

        return farmer

    @staticmethod
    def reject_farmer(farmer):
        """
        Reject supplier.
        """

        farmer.verification_status = FarmerStatus.REJECTED
        farmer.verified_at = None

        farmer.save(
            update_fields=[
                "verification_status",
                "verified_at",
            ]
        )

        return farmer

    @staticmethod
    def deactivate_farmer(farmer):
        """
        Soft deactivate supplier.
        """

        farmer.is_active = False
        farmer.save(update_fields=["is_active"])

        return farmer

    @staticmethod
    def activate_farmer(farmer):
        """
        Activate supplier.
        """

        farmer.is_active = True
        farmer.save(update_fields=["is_active"])

        return farmer