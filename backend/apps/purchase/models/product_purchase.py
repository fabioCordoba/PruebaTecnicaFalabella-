from django.db import models
from apps.product.models.product import Product
from apps.purchase.models.purchase import Purchase

class ProductPurchase(models.Model):

    purchase = models.ForeignKey(
        Purchase, 
        on_delete=models.CASCADE, 
        related_name='product_purchases'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Producto en compra"
        verbose_name_plural = "Productos en compra"
        unique_together = ('purchase', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Compra {self.purchase.code})"