from django.contrib import admin

from apps.document_type.models.document_type import DocumentType

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "short_name",
        "is_active",
    ]
