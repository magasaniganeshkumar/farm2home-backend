from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from apps.core.models import BaseModel


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
        max_length=10,
        unique=True,
        help_text="Unique category code. Example: VEG, FRT, RICE.",
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
        help_text="Category hierarchy level.",
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
        help_text="Whether this category is active.",
    )

    is_visible = models.BooleanField(
        default=True,
        help_text="Whether this category is visible to customers.",
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
        """
        Prevent invalid hierarchy.
        """
        if self.parent == self:
            raise ValidationError(
                "A category cannot be its own parent."
            )

    def save(self, *args, **kwargs):
        """
        Auto-generate slug and category level.
        """
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