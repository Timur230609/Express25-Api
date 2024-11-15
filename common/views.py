from rest_framework import generics,permissions
from .serializers import AddressSerializer, PlasticCardSerializer
from .models import Address, PlasticCard

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Address
    lookup_field = 'id'

class AddressListAPIView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlasticCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlasticCardSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PlasticCard
    lookup_field = 'id'
    def get_queryset(self):
        return PlasticCard.objects.filter(user=self.request.user) 

    
class PlasticCardListAPIView(generics.ListCreateAPIView):
    queryset = PlasticCard.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlasticCardSerializer

    def get_queryset(self):
        return PlasticCard.objects.filter(user=self.request.user)    
    
