from django.utils import timezone

from .models import Farmer, FarmerStatus


class FarmerService:
    """
    Farmer business logic.
    """

    @staticmethod
    def create_farmer(validated_data):
        """
        Create a new farmer profile.
        """
        return Farmer.objects.create(**validated_data)

    @staticmethod
    def update_farmer(farmer, validated_data):
        """
        Update farmer profile.
        """
        for field, value in validated_data.items():
            setattr(farmer, field, value)

        farmer.save()
        return farmer

    @staticmethod
    def verify_farmer(farmer):
        """
        Verify farmer.
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
        Reject farmer.
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
        Soft deactivate farmer.
        """
        farmer.is_active = False
        farmer.save(update_fields=["is_active"])
        return farmer

    @staticmethod
    def activate_farmer(farmer):
        """
        Activate farmer.
        """
        farmer.is_active = True
        farmer.save(update_fields=["is_active"])
        return farmer