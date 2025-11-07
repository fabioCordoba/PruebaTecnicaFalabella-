from django.db import models
import random
import string
from apps.core.models.base_model import BaseModel
from apps.users.models.user import User
from decimal import Decimal

def generate_code(name):
    initials = "".join([word[0] for word in name.split()])[:3].upper()
    numbers = "".join(random.choices(string.digits, k=5))
    return f"{initials}-{numbers}"


class Purchase(BaseModel):
    code = models.CharField(max_length=255, unique=True, blank=True, null=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="client",
        related_name='purchases'
    )
    total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Compra {self.code} - {self.user.username}"
    
    def calculate_total(self):

        total = sum(
            item.product.price * item.quantity for item in self.product_purchases.all()
        )
        self.total = total
        self.save()
        return total
    
    def save(self, *args, **kwargs):
        if not self.code:
            name = self.user.get_full_name() or self.user.username
            new_code = generate_code(name)

            while Purchase.objects.filter(code=new_code).exists():
                new_code = generate_code(name)

            self.code = new_code

        super().save(*args, **kwargs)