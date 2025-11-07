from rest_framework import viewsets, mixins
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from apps.core.permissions.permissions import IsAdminOrReadOnly, IsSuperOrReadOnly
from apps.product.models.product import Product
from apps.product.serializers.product_serializers import ProductSerializer


class ProductViewSet(
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
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.is_active = False
        product.save(update_fields=["is_active"])
        return Response(
            {"detail": f"El Producto {product.name} ha sido desactivado."},
            status=status.HTTP_200_OK,
        )



