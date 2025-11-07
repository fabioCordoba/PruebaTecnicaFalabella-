from django.urls import include, path
from rest_framework import routers

from apps.purchase.api.views import PurchaseViewSet

router = routers.DefaultRouter()
router.register(r"purchase", PurchaseViewSet, basename="purchase")

urlpatterns = [
    path("", include(router.urls)),
]
