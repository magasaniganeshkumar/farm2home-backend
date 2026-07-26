from django.db import models

from apps.core.models import BaseModel


class BusinessSequence(BaseModel):
    """
    Stores sequence numbers for business entities.
    """

    class Entity(models.TextChoices):
        CATEGORY = "CATEGORY", "Category"
        PRODUCT = "PRODUCT", "Product"
        SUPPLIER = "SUPPLIER", "Supplier"
        LISTING = "LISTING", "Listing"
        LOCATION = "LOCATION", "Location"
        ORDER = "ORDER", "Order"
        PAYMENT = "PAYMENT", "Payment"

    entity = models.CharField(
        max_length=30,
        choices=Entity.choices,
        unique=True,
        db_index=True,
    )

    prefix = models.CharField(
        max_length=10,
    )

    last_number = models.PositiveBigIntegerField(
        default=0,
    )

    class Meta:
        db_table = "business_sequences"
        ordering = ["entity"]
        verbose_name = "Business Sequence"
        verbose_name_plural = "Business Sequences"

    def __str__(self):
        return (
            f"{self.entity} "
            f"[{self.prefix}-{self.last_number:06d}]"
        )