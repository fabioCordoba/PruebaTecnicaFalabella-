from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models.base_model import BaseModel
from apps.document_type.models.document_type import DocumentType


class User(BaseModel, AbstractUser):
    ROLES = (
        ("administrator", "Administrator"),
        ("guest", "Guest"),
    )
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    document_number = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
    )
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=13, choices=ROLES)
    image = models.ImageField(
        upload_to="user/",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
