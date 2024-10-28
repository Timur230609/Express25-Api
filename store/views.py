from django.shortcuts import render
from django.views import View
from store.models import Category
from django.http import JsonResponse



class StoreDetailView(View):

    def get(self, request, id):
        store = Category.objects.get(id=id,category_type='Store')
        json_response = {
            'name':store.name,
            'address':{'city':store.address.city,
                       'district':store.address.district},
            'description':store.description,
            'phone_number':store.phone_number,
            'rating':store.rating
        }
        return JsonResponse(json_response)
    
    #delete, put, patch


    
class StoreListAPIView(View):
    def get(self, request):
        stores = Category.objects.filter(category_type='Store')
        json_responses = list()
        for store in stores:
            json_response = {
                'name':store.name,
                'address':{'city':store.address.city,
                        'district':store.address.district},
                'description':store.description,
                'phone_number':store.phone_number,
                'rating':store.rating
            }
            json_responses.append(json_response)


        return JsonResponse(json_responses,safe=False)
    
    #post
    
#postman