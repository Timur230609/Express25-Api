from rest_framework import viewsets, permissions
from .models import Address, PlasticCard
from .serializers import AddressSerializer, PlasticCardSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)  # Filter by logged-in user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Save with the logged-in user


class PlasticCardViewSet(viewsets.ModelViewSet):
    queryset = PlasticCard.objects.all()
    serializer_class = PlasticCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PlasticCard.objects.filter(user=self.request.user)  # Filter by logged-in user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Save with the logged-in user
