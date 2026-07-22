from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.core.models import BaseModel
from .managers import UserManager


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