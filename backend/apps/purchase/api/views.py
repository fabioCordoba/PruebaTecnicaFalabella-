from rest_framework import viewsets, mixins
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.core.permissions.permissions import IsAdminOrReadOnly, IsSuperOrReadOnly
from apps.purchase.models.purchase import Purchase
from apps.purchase.serializers.purchase_serializers import PurchaseSerializer
from apps.users.models.user import User


class PurchaseViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint to list, view, update, and delete loan.
    """

    permission_classes = [IsAuthenticated, IsSuperOrReadOnly, IsAdminOrReadOnly]
    queryset = Purchase.objects.filter(is_active=True)
    serializer_class = PurchaseSerializer

    def destroy(self, request, *args, **kwargs):
        purchase = self.get_object()
        purchase.is_active = False
        purchase.save(update_fields=["is_active"])
        return Response(
            {"detail": f"La compra {purchase.code} ha sido desactivado."},
            status=status.HTTP_200_OK,
        )


class PurchasesByDocumentView(APIView):
    def get(self, request, document_number):
        try:
            user = User.objects.get(document_number=document_number)
        except User.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        purchases = Purchase.objects.filter(user=user).prefetch_related("product_purchases__product")
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)