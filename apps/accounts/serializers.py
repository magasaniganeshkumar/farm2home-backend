from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.mail import send_mail

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import PasswordResetToken
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


class UserLoginSerializer(TokenObtainPairSerializer):
    """
    Custom JWT Login Serializer.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email
        token["user_type"] = user.user_type

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data["message"] = "Login successful."
        data["user"] = {
            "id": str(self.user.id),
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "phone_number": self.user.phone_number,
            "user_type": self.user.user_type,
        }

        return data

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for authenticated user's profile.
    """

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "phone_number",
            "user_type",
            "is_verified",
        )
        read_only_fields = fields

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()


class UserLogoutSerializer(serializers.Serializer):
    """
    Logout serializer.
    Blacklists the refresh token.
    """

    refresh = serializers.CharField()

    def validate(self, attrs):
        self.refresh_token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.refresh_token)
            token.blacklist()
        except Exception:
            raise serializers.ValidationError(
                {"refresh": "Invalid or expired refresh token."}
            )


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        write_only=True,
        required=True,
    )
    new_password = serializers.CharField(
        write_only=True,
        required=True,
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
    )

    def validate(self, attrs):
        user = self.context["request"].user

        if not user.check_password(attrs["current_password"]):
            raise serializers.ValidationError(
                {"current_password": "Current password is incorrect."}
            )

        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )

        try:
            validate_password(attrs["new_password"], user)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(
                {"new_password": list(exc.messages)}
            )

        return attrs

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save(update_fields=["password"])
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "No account found with this email."
            )
        return value

    def save(self):
        reset_token = PasswordResetToken.create_token(self.user)

        reset_link = (
            f"http://127.0.0.1:8000/api/v1/accounts/reset-password/"
            f"?token={reset_token.token}"
        )

        send_mail(
            subject="Farm2Home Password Reset",
            message=(
                f"Hello {self.user.first_name},\n\n"
                f"Click the link below to reset your password:\n\n"
                f"{reset_link}\n\n"
                "This link will expire in 1 hour."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

        return reset_token


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(
        write_only=True,
        min_length=8,
    )
    confirm_password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password": "Passwords do not match."
                }
            )

        try:
            validate_password(attrs["new_password"])
        except DjangoValidationError as exc:
            raise serializers.ValidationError(
                {
                    "new_password": list(exc.messages)
                }
            )

        try:
            reset_token = PasswordResetToken.objects.get(
                token=attrs["token"]
            )
        except PasswordResetToken.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "token": "Invalid reset token."
                }
            )

        if not reset_token.is_valid():
            raise serializers.ValidationError(
                {
                    "token": "Reset token has expired or has already been used."
                }
            )

        self.reset_token = reset_token
        return attrs

    def save(self):
        user = self.reset_token.user

        user.set_password(
            self.validated_data["new_password"]
        )
        user.save(update_fields=["password"])

        self.reset_token.is_used = True
        self.reset_token.save(update_fields=["is_used"])

        return user