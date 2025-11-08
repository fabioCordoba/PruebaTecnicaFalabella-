
from rest_framework import viewsets, mixins
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from apps.core.permissions.permissions import IsAdminOrReadOnly, IsSuperOrReadOnly
from apps.document_type.serializers.document_serializers import DocuemntTypeSerializer
from apps.document_type.models.document_type import DocumentType


class DocumentTypeViewSet(
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

    # permission_classes = [IsAuthenticated, IsSuperOrReadOnly, IsAdminOrReadOnly]
    queryset = DocumentType.objects.filter(is_active=True)
    serializer_class = DocuemntTypeSerializer

    def destroy(self, request, *args, **kwargs):
        document = self.get_object()
        document.is_active = False
        document.save(update_fields=["is_active"])
        return Response(
            {"detail": f"El tipo de documento {document.name} ha sido desactivado."},
            status=status.HTTP_200_OK,
        )

