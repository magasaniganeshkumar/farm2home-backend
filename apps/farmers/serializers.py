from rest_framework import serializers

from .models import Farmer


class SupplierApplicationSerializer(serializers.ModelSerializer):
    """
    Customer applies to become a supplier.
    """

    class Meta:
        model = Farmer
        fields = (
            "farming_type",
            "other_farming_type",
            "experience_years",
            "preferred_language",
            "alternate_phone_number",
            "preferred_payment_method",
        )


def validate(self, attrs):
    protected = self.PROTECTED_FIELDS.intersection(
        self.initial_data.keys()
    )

    if protected:
        raise serializers.ValidationError(
            {
                field: "This field cannot be updated."
                for field in protected
            }
        )

    return attrs
class FarmerUpdateSerializer(serializers.ModelSerializer):
    """
    Update Supplier Profile
    """

    PROTECTED_FIELDS = {
        "verification_status",
        "verified_at",
        "farmer_code",
        "user",
        "is_active",
        "created_at",
        "updated_at",
    }

    class Meta:
        model = Farmer
        fields = (
            "farming_type",
            "other_farming_type",
            "experience_years",
            "preferred_language",
            "alternate_phone_number",
            "preferred_payment_method",
        )

    def validate(self, attrs):
        protected = self.PROTECTED_FIELDS.intersection(
            self.initial_data.keys()
        )

        if protected:
            raise serializers.ValidationError(
                {
                    field: ["This field cannot be updated."]
                    for field in protected
                }
            )

        return attrs


class FarmerListSerializer(serializers.ModelSerializer):
    """
    Supplier List Serializer
    """

    full_name = serializers.CharField(
        source="user.full_name",
        read_only=True,
    )

    phone_number = serializers.CharField(
        source="user.phone_number",
        read_only=True,
    )

    class Meta:
        model = Farmer
        fields = (
            "id",
            "farmer_code",
            "full_name",
            "phone_number",
            "farming_type",
            "verification_status",
            "is_active",
        )


class FarmerDetailSerializer(serializers.ModelSerializer):
    """
    Supplier Detail Serializer
    """

    full_name = serializers.CharField(
        source="user.full_name",
        read_only=True,
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )

    phone_number = serializers.CharField(
        source="user.phone_number",
        read_only=True,
    )

    class Meta:
        model = Farmer
        fields = (
            "id",
            "farmer_code",
            "full_name",
            "email",
            "phone_number",
            "alternate_phone_number",
            "farming_type",
            "experience_years",
            "preferred_language",
            "preferred_payment_method",
            "verification_status",
            "verified_at",
            "is_active",
            "created_at",
            "updated_at",
        )


class FarmerVerificationSerializer(serializers.ModelSerializer):
    """
    Admin Verification Serializer
    """

    class Meta:
        model = Farmer
        fields = (
            "verification_status",
        )