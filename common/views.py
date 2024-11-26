from rest_framework import viewsets, permissions, pagination
from rest_framework.response import Response
from .models import Address, PlasticCard
from .serializers import AddressSerializer, PlasticCardSerializer


class StandardResultsPagination(pagination.PageNumberPagination):
    """
    Custom pagination class to control the number of items per page.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        """
        Only return addresses related to the logged-in user.
        """
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the user as the owner of the new address.
        """
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        Override to include paginated response.
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PlasticCardViewSet(viewsets.ModelViewSet):
    serializer_class = PlasticCardSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        """
        Only return plastic cards related to the logged-in user.
        """
        return PlasticCard.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the user as the owner of the new plastic card.
        """
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        Override to include paginated response.
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
