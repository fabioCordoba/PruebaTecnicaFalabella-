from rest_framework import serializers

from apps.users.models.user import User
from apps.users.serializers.user_serializers import UserSerializer
from apps.purchase.models.purchase import Purchase
from apps.purchase.models.product_purchase import ProductPurchase


# class PurchaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase
#         fields = [
#             "id",
#             "code",
#             "user",
#             "total",
#             "created_at",
#             "updated_at",
#         ]

class ProductPurchaseSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(
        source="product.price", max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = ProductPurchase
        fields = ["product_name", "product_price", "quantity"]


class PurchaseSerializer(serializers.ModelSerializer):
    products = ProductPurchaseSerializer(
        source="product_purchases", many=True, read_only=True
    )

    class Meta:
        model = Purchase
        fields = ["code", "total", "created_at", "products"]