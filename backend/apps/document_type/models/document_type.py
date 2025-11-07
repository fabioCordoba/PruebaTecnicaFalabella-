from django.db import models
from apps.core.models.base_model import BaseModel

class DocumentType(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="name"
    )
    short_name = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="form"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.short_name} - {self.name}"
