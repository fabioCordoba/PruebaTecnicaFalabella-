from django.contrib import admin

from apps.purchase.models.purchase import Purchase
from apps.purchase.models.product_purchase import ProductPurchase


class ProductPurchaseInline(admin.TabularInline):
    model = ProductPurchase
    extra = 1  # Muestra un campo vacío adicional
    autocomplete_fields = ["product"]  # Requiere search_fields en ProductAdmin
    readonly_fields = ["subtotal"]

    def subtotal(self, obj):
        if obj.product:
            return obj.product.price * obj.quantity
        return "-"
    subtotal.short_description = "Subtotal"

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["code", "user", "total", "created_at"]
    inlines = [ProductPurchaseInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Recalcular el total al guardar
        obj.calculate_total()

# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = [
#         "code",
#         "user",
#         "total",
#         "created_at",
#     ]