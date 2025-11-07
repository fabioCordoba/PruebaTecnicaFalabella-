from rest_framework import serializers

from apps.users.models.user import User
from apps.users.serializers.user_serializers import UserSerializer
from apps.document_type.models.document_type import DocumentType


class DocuemntTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = [
            "id",
            "name",
            "short_name",
        ]
