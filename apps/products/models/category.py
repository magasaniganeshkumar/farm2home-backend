from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from apps.core.models import BaseModel
from apps.infrastructure.services.code_service import CodeService


class Category(BaseModel):
    """
    Master Product Category.

    Examples:
    - Vegetables
    - Fruits
    - Rice & Grains
    - Dairy
    - Oil Seeds
    """

    code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        editable=False,
    )

    name = models.CharField(
        max_length=100,
        help_text="Category display name.",
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True,
    )

    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional icon name for mobile/web.",
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="subcategories",
        help_text="Parent category (optional).",
    )

    level = models.PositiveSmallIntegerField(
        default=0,
        editable=False,
    )

    display_order = models.PositiveIntegerField(
        default=0,
        db_index=True,
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_visible = models.BooleanField(
        default=True,
    )

    seo_title = models.CharField(
        max_length=255,
        blank=True,
    )

    seo_description = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "product_categories"

        verbose_name = "Category"
        verbose_name_plural = "Categories"

        ordering = [
            "display_order",
            "name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["parent", "name"],
                name="unique_category_per_parent",
            )
        ]

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["parent"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["is_visible"]),
            models.Index(fields=["is_featured"]),
        ]

    def clean(self):
        if self.parent == self:
            raise ValidationError(
                "A category cannot be its own parent."
            )

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = CodeService.next_category_code()

        if not self.slug:
            self.slug = slugify(self.name)

        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name