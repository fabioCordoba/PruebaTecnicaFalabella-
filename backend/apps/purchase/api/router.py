from django.urls import include, path
from rest_framework import routers

from apps.purchase.api.views import PurchaseViewSet, PurchasesByDocumentView

router = routers.DefaultRouter()
router.register(r"purchase", PurchaseViewSet, basename="purchase")

urlpatterns = [
    path("", include(router.urls)),
    path("purchases/<str:document_number>/", PurchasesByDocumentView.as_view(), name="purchases-by-document"),
]
