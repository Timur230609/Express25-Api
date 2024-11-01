from store.models import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from store.serializers import StoreSerializer
from rest_framework import status,generics

# class StoreDetailView(View):

#     def get(self, request, id):
#         store = Category.objects.get(id=id,category_type='Store')
#         json_response = {
#             'name':store.name,
#             'address':{'city':store.address.city,
#                        'district':store.address.district},
#             'description':store.description,
#             'phone_number':store.phone_number,
#             'rating':store.rating
#         }
#         return JsonResponse(json_response)
    
#     #delete, put, patch

class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Category
    lookup_field = 'id'
    
# class StoreDetailView(APIView):

#     def get(self, request, id):
#         store = Category.objects.get(id=id,category_type='Store')
#         serializer = StoreSerializer(store)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def delete(self, request, id, format=None):
#         store = Category.objects.get(id=id,category_type='Store')
#         store.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, id, format=None):
#         store = Category.objects.get(id=id,category_type='Store')
#         serializer = StoreSerializer(store, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, id, format=None):
#         store = Category.objects.get(id=id,category_type='Store')
#         serializer = StoreSerializer(store, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete, put, patch


    
# class StoreListAPIView(View):
#     def get(self, request):
#         stores = Category.objects.filter(category_type='Store')
#         json_responses = list()
#         for store in stores:
#             json_response = {
#                 'name':store.name,
#                 'address':{'city':store.address.city,
#                         'district':store.address.district},
#                 'description':store.description,
#                 'phone_number':store.phone_number,
#                 'rating':store.rating
#             }
#             json_responses.append(json_response)


#         return JsonResponse(json_responses,safe=False)
    
#     #post

# class StoreListAPIView(APIView):

#     def get(self, request):
#         stores = Category.objects.filter(category_type='Store')
#         serializer = StoreSerializer(stores, many=True)

#         return Response(data=serializer.data,status=status.HTTP_200_OK)
    

#     def post(self, request, format=None):
#         serializer = StoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #post

class StoreListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(category_type='Store')
    serializer_class = StoreSerializer




#postman