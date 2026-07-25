from django.contrib import admin

from .models import Farmer


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = (
        "farmer_code",
        "user",
        "farming_type",
        "verification_status",
        "preferred_payment_method",
        "is_active",
    )

    list_filter = (
        "farming_type",
        "verification_status",
        "preferred_payment_method",
        "is_active",
    )

    search_fields = (
        "farmer_code",
        "user__first_name",
        "user__last_name",
        "user__email",
        "user__phone_number",
    )

    readonly_fields = (
        "farmer_code",
        "created_at",
        "updated_at",
    )

    ordering = ("farmer_code",)