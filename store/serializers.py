from rest_framework import serializers
from store.models import Category
from common.serializers import AddressSerializer



class StoreSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    address_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Category
        
        fields =  "__all__"
    def validate(self, data):
        # addressni tekshirasilar
        address_id = data.get("address")
        if Category.objects.filter(address_id = address_id).exists():
            raise serializers.ValidationError('Address topilmadi')
        phone_number = data.get("phone_number")
        if Category.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("Bu telefon nomerdan Dokon yaratilgan")


        return super().validate(data)
    


    



