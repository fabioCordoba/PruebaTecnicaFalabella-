from django.contrib import admin

from apps.product.models.product import Product


@admin.register(Product)
class LoanAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "price",
        "stock",
        "created_at",
        "updated_at",
        "is_active",
    ]
