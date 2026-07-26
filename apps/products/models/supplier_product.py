from django.core.exceptions import ValidationError
from django.db import models

from apps.core.models import BaseModel
from apps.farmers.models import Farmer
from apps.infrastructure.services.code_service import CodeService

from apps.products.choices import (
    ProductGrade,
    SupplierProductStatus,
)

from .product import Product


class SupplierProduct(BaseModel):
    """
    Supplier's listing for a catalog product.
    One supplier can have only one listing for a product.
    """

    listing_code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name="supplier_products",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="supplier_products",
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    available_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    minimum_order_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1,
    )

    estimated_delivery_days = models.PositiveSmallIntegerField(
        default=1,
    )

    pickup_available = models.BooleanField(
        default=False,
    )

    home_delivery = models.BooleanField(
        default=True,
    )

    is_organic = models.BooleanField(
        default=False,
    )

    is_certified = models.BooleanField(
        default=False,
    )

    grade = models.CharField(
        max_length=20,
        choices=ProductGrade.choices,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    notes = models.TextField(
        blank=True,
        help_text="Additional information from the supplier.",
    )

    harvest_date = models.DateField(
        null=True,
        blank=True,
    )

    available_from = models.DateField(
        null=True,
        blank=True,
    )

    available_until = models.DateField(
        null=True,
        blank=True,
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    rejected_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=30,
        choices=SupplierProductStatus.choices,
        default=SupplierProductStatus.DRAFT,
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_visible = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "supplier_products"

        ordering = [
            "-created_at",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["farmer", "product"],
                name="unique_farmer_product",
            ),
        ]

        indexes = [
            models.Index(fields=["listing_code"]),
            models.Index(fields=["farmer"]),
            models.Index(fields=["product"]),
            models.Index(fields=["status"]),
            models.Index(fields=["selling_price"]),
            models.Index(fields=["is_organic"]),
            models.Index(fields=["is_visible"]),
            models.Index(fields=["is_featured"]),
        ]

    def clean(self):
        if (
            self.discount_price is not None
            and self.discount_price > self.selling_price
        ):
            raise ValidationError(
                "Discount price cannot be greater than selling price."
            )

        if self.available_quantity < 0:
            raise ValidationError(
                "Available quantity cannot be negative."
            )

        if self.minimum_order_quantity <= 0:
            raise ValidationError(
                "Minimum order quantity must be greater than zero."
            )

        if (
            self.available_from
            and self.available_until
            and self.available_from > self.available_until
        ):
            raise ValidationError(
                "Available from date cannot be after available until date."
            )

    def save(self, *args, **kwargs):
        if not self.listing_code:
            self.listing_code = (
                CodeService.next_listing_code()
            )

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.listing_code} | "
            f"{self.farmer.user.full_name} | "
            f"{self.product.name}"
        )