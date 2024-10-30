from rest_framework import serializers
from store.models import Category
from common.serializers import AddressSerializer



class StoreSerializer(serializers.ModelSerializer):
    # address = AddressSerializer(readonly=True)
    class Meta:
        model = Category
        fields =  "__all__"


