from django.conf import settings
from django.db import models

from apps.core.models import BaseModel


class FarmerStatus(models.TextChoices):
    PENDING = "PENDING", "Pending Verification"
    VERIFIED = "VERIFIED", "Verified"
    REJECTED = "REJECTED", "Rejected"


class FarmingType(models.TextChoices):
    CROPS = "CROPS", "Crops"
    VEGETABLES = "VEGETABLES", "Vegetables"
    FRUITS = "FRUITS", "Fruits"
    ORGANIC = "ORGANIC", "Organic Farming"
    DAIRY = "DAIRY", "Dairy"
    POULTRY = "POULTRY", "Poultry"
    FISHERIES = "FISHERIES", "Fisheries"
    HONEY = "HONEY", "Honey & Beekeeping"
    FLOWERS = "FLOWERS", "Flowers"
    SPICES = "SPICES", "Spices"
    HERBS = "HERBS", "Herbs"
    PLANT_NURSERY = "PLANT_NURSERY", "Plant Nursery"
    MIXED = "MIXED", "Mixed Farming"
    OTHER = "OTHER", "Other"


class PaymentMethod(models.TextChoices):
    BANK_TRANSFER = "BANK_TRANSFER", "Bank Transfer"
    UPI = "UPI", "UPI"
    CASH = "CASH", "Cash"
    CHEQUE = "CHEQUE", "Cheque"


class Farmer(BaseModel):
    """
    Farmer profile.
    User personal details are stored in the User model.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="farmer_profile",
    )

    farmer_code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )

    farming_type = models.CharField(
        max_length=20,
        choices=FarmingType.choices,
    )
    other_farming_type = models.CharField(
        max_length=100,
        blank=True,
    )

    experience_years = models.PositiveIntegerField(
        default=0,
    )

    preferred_language = models.CharField(
        max_length=50,
        default="Telugu",
    )

    alternate_phone_number = models.CharField(
        max_length=15,
        blank=True,
    )

    preferred_payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.BANK_TRANSFER,
    )

    verification_status = models.CharField(
        max_length=20,
        choices=FarmerStatus.choices,
        default=FarmerStatus.PENDING,
    )

    verified_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "farmers"
        ordering = ["farmer_code"]

    def save(self, *args, **kwargs):
        if not self.farmer_code:
            last_farmer = (
                Farmer.all_objects.order_by("-created_at").first()
            )

            if last_farmer:
                last_number = int(last_farmer.farmer_code.split("-")[1])
                next_number = last_number + 1
            else:
                next_number = 1

            self.farmer_code = f"FARM-{next_number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.farmer_code} - {self.user.full_name}"