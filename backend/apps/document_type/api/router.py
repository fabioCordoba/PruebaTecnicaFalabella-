from django.urls import include, path
from rest_framework import routers

from apps.document_type.api.views import DocumentTypeViewSet



router = routers.DefaultRouter()
router.register(r"docment_type", DocumentTypeViewSet, basename="docment_type")

urlpatterns = [
    path("", include(router.urls)),
]
