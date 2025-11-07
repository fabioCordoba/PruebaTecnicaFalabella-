from django.contrib import admin

from apps.purchase.models.purchase import Purchase




@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "user",
        "total",
        "created_at",
    ]