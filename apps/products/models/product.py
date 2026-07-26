from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from apps.core.models import BaseModel
from apps.infrastructure.services.code_service import CodeService

from apps.products.choices import (
    CatalogStatus,
    ProductSeason,
    ProductType,
    ProductUnit,
    StorageType,
)

from .category import Category


class Product(BaseModel):
    """
    Farm2Home Product Catalog.

    One product can be supplied by many suppliers.
    """

    product_code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )

    name = models.CharField(
        max_length=150,
        db_index=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )

    product_type = models.CharField(
        max_length=30,
        choices=ProductType.choices,
    )

    short_description = models.CharField(
        max_length=255,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    default_unit = models.CharField(
        max_length=20,
        choices=ProductUnit.choices,
    )

    storage_type = models.CharField(
        max_length=30,
        choices=StorageType.choices,
        default=StorageType.AMBIENT,
    )

    season = models.CharField(
        max_length=30,
        choices=ProductSeason.choices,
        default=ProductSeason.YEAR_ROUND,
    )

    shelf_life_days = models.PositiveIntegerField(
        default=0,
    )

    is_perishable = models.BooleanField(
        default=True,
    )

    hsn_code = models.CharField(
        max_length=20,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=CatalogStatus.choices,
        default=CatalogStatus.ACTIVE,
    )

    is_featured = models.BooleanField(
        default=False,
    )

    seo_title = models.CharField(
        max_length=255,
        blank=True,
    )

    seo_description = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "products"

        verbose_name = "Product"
        verbose_name_plural = "Products"

        ordering = [
            "name",
        ]

        indexes = [
            models.Index(fields=["product_code"]),
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["category"]),
            models.Index(fields=["product_type"]),
            models.Index(fields=["status"]),
            models.Index(fields=["is_featured"]),
        ]

    def clean(self):
        if self.shelf_life_days < 0:
            raise ValidationError(
                "Shelf life cannot be negative."
            )

    def save(self, *args, **kwargs):

        if not self.product_code:
            self.product_code = (
                CodeService.next_product_code()
            )

        if not self.slug:
            self.slug = slugify(self.name)

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name