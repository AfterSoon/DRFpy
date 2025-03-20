from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import PaymentViewSet, UserCreateAPIView

app_name = "users"

router = DefaultRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path("payment/create/", UserCreateAPIView.as_view(), name="payment_create")
] + router.urls