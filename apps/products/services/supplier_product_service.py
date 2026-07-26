from django.db import transaction

from apps.products.models import SupplierProduct
from apps.products.choices import SupplierProductStatus


class SupplierProductService:
    """
    Business logic for supplier product listings.
    """

    @staticmethod
    @transaction.atomic
    def create_listing(*, farmer, validated_data):
        """
        Create a new supplier product listing.
        """
        return SupplierProduct.objects.create(
            farmer=farmer,
            **validated_data,
        )

    @staticmethod
    @transaction.atomic
    def update_listing(*, listing, validated_data):
        """
        Update an existing supplier listing.
        """
        for field, value in validated_data.items():
            setattr(listing, field, value)

        listing.save()

        return listing

    @staticmethod
    @transaction.atomic
    def submit_for_review(*, listing):
        """
        Submit a listing for admin review.
        """
        listing.status = SupplierProductStatus.SUBMITTED
        listing.save(update_fields=["status"])

        return listing

    @staticmethod
    @transaction.atomic
    def approve_listing(*, listing):
        """
        Approve a supplier listing.
        """
        listing.status = SupplierProductStatus.APPROVED
        listing.is_visible = True
        listing.save(
            update_fields=[
                "status",
                "is_visible",
            ]
        )

        return listing

    @staticmethod
    @transaction.atomic
    def reject_listing(*, listing):
        """
        Reject a supplier listing.
        """
        listing.status = SupplierProductStatus.REJECTED
        listing.is_visible = False
        listing.save(
            update_fields=[
                "status",
                "is_visible",
            ]
        )

        return listing