from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Farmer

User = get_user_model()


class FarmerCreateSerializer(serializers.ModelSerializer):
    """
    Create Farmer Profile
    """

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(
            user_type=User.UserType.CUSTOMER
        )
    )

    class Meta:
        model = Farmer
        fields = (
            "id",
            "user",
            "farming_type",
            "experience_years",
            "preferred_language",
            "alternate_phone_number",
            "preferred_payment_method",
        )
        read_only_fields = (
            "id",
        )

    def validate_user(self, value):
        if Farmer.objects.filter(user=value).exists():
            raise serializers.ValidationError(
                "This user already has a farmer profile."
            )
        return value


class FarmerUpdateSerializer(serializers.ModelSerializer):
    """
    Update Farmer Profile
    """

    class Meta:
        model = Farmer
        fields = (
            "farming_type",
            "experience_years",
            "preferred_language",
            "alternate_phone_number",
            "preferred_payment_method",
        )


class FarmerListSerializer(serializers.ModelSerializer):
    """
    Farmer List Serializer
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
    Farmer Detail Serializer
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