from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Delivery
from .serializers import DeliverySerializer
from rest_framework import generics
from .models import Delivery


# class DeliveryListCreateAPIView(APIView):
#     def get(self, request):
#         deliveries = Delivery.objects.all()
#         serializer = DeliverySerializer(deliveries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = DeliverySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DeliveryDetailAPIView(APIView):
#     def get_object(self, id):
#         return get_object_or_404(Delivery, id=id)

#     def get(self, request, id):
#         delivery = self.get_object(id)
#         serializer = DeliverySerializer(delivery)
#         return Response(serializer.data)

#     def put(self, request, id):
#         delivery = self.get_object(id)
#         serializer = DeliverySerializer(delivery, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         delivery = self.get_object(id)
#         delivery.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class DeliveryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'id'