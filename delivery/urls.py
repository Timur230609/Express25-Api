from django.urls import path
from .views import DeliveryListCreateAPIView, DeliveryDetailAPIView

urlpatterns = [
    path('deliveries/', DeliveryListCreateAPIView.as_view(), name='delivery-list-create'),
    path('deliveries/<int:id>/', DeliveryDetailAPIView.as_view(), name='delivery-detail'),
]