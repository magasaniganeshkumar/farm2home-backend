from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            "id",
            "location_type",
            "display_name",
            "contact_person",
            "contact_number",
            "house_number",
            "street",
            "landmark",
            "locality",
            "city",
            "district",
            "state",
            "country",
            "postal_code",
            "latitude",
            "longitude",
            "delivery_instructions",
            "is_default",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )