"""
Base Models for all things
"""

from uuid import uuid4
# from datetime import datetime
# from django.utils.translation import gettext as _
# from django.core.exceptions import ValidationError
# from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


account_type_choices = (("Student", "Student"), ("Library Staff", "Library Staff"))


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid4, editable=False
    )
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    account_type = models.CharField(
        max_length=50, choices=account_type_choices, default="Student"
    )
    email_confirmed = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
