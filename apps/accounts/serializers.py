from django.contrib.auth import get_user_model
from rest_framework import serializers
from .services import UserService

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"},
    )

    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "role",
            "password",
            "confirm_password",
        )

    def validate(self, attrs):
        """
        Validate password confirmation.
        """
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        return UserService.create_user(validated_data)