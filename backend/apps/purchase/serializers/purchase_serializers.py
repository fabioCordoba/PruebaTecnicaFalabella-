from rest_framework import serializers

from apps.users.models.user import User
from apps.users.serializers.user_serializers import UserSerializer
from apps.purchase.models.purchase import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = [
            "id",
            "code",
            "user",
            "total",
            "created_at",
            "updated_at",
        ]

