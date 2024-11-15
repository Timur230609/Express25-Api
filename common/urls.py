from .views import AddressViewSet, PlasticCardViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Define routers
router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'plastic-cards', PlasticCardViewSet, basename='plasticcard')

# Manually add custom paths if required
custom_urlpatterns = [
    path('addresses/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve'}), name='address-detail'),
    path('plastic-cards/<int:pk>/', PlasticCardViewSet.as_view({'get': 'retrieve'}), name='plastic-card-detail'),
]

urlpatterns = [
    path('', include(router.urls)),
] + custom_urlpatterns
