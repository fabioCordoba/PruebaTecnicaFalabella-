from django.db import models
from apps.core.models.base_model import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} (${self.price})"