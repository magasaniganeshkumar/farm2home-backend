from django.contrib import admin

from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "display_name",
        "user",
        "location_type",
        "city",
        "state",
        "is_default",
        "is_active",
    )

    list_filter = (
        "location_type",
        "state",
        "is_default",
        "is_active",
    )

    search_fields = (
        "display_name",
        "user__email",
        "city",
        "district",
        "postal_code",
    )

    ordering = ("-created_at",)