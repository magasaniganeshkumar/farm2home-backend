from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.core.models import BaseModel
from .managers import UserManager

import secrets
from datetime import timedelta

from django.utils import timezone


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        FARMER = "FARMER", "Farmer"
        CUSTOMER = "CUSTOMER", "Customer"

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.CUSTOMER,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class PasswordResetToken(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="password_reset_tokens",
    )
    token = models.CharField(
        max_length=128,
        unique=True,
    )
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    @classmethod
    def create_token(cls, user):
        return cls.objects.create(
            user=user,
            token=secrets.token_urlsafe(48),
            expires_at=timezone.now() + timedelta(hours=1),
        )

    def is_valid(self):
        return (
            not self.is_used
            and timezone.now() < self.expires_at
        )

    def __str__(self):
        return f"{self.user.email} - Password Reset"