from django.conf import settings
from django.db import models

from apps.core.models import BaseModel


class LocationType(models.TextChoices):
    HOME = "HOME", "Home"
    OFFICE = "OFFICE", "Office"
    OTHER = "OTHER", "Other"


class Location(BaseModel):
    """
    Customer delivery address.
    Future modules (Farm, Hub) will have their own models.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="locations",
    )

    location_type = models.CharField(
        max_length=20,
        choices=LocationType.choices,
        default=LocationType.HOME,
    )

    display_name = models.CharField(
        max_length=100,
        help_text="Example: Home, Office, Parents House",
    )

    contact_person = models.CharField(
        max_length=100,
    )

    contact_number = models.CharField(
        max_length=15,
    )

    house_number = models.CharField(
        max_length=100,
    )

    street = models.CharField(
        max_length=255,
    )

    landmark = models.CharField(
        max_length=255,
        blank=True,
    )

    locality = models.CharField(
        max_length=150,
        blank=True,
    )

    city = models.CharField(
        max_length=100,
    )

    district = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    postal_code = models.CharField(
        max_length=10,
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    delivery_instructions = models.TextField(
        blank=True,
    )

    is_default = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "locations"
        ordering = ["-created_at"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.display_name} - {self.city}"