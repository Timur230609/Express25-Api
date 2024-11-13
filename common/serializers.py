from rest_framework import serializers
from .models import Address,PlasticCard
from datetime import date
from accaunt.serializers import RegisterSerializer



#user ni malumotlarini obyekt sifatida ko'ra olamiz
#ma'lumot qo'shishda user_id sidan foydalanishimiz kerak
class AddressSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Address
        fields =  "__all__"


class PlasticCardSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = PlasticCard
        fields =  "__all__"

    def validate(self, data):
        expiration_date = data.get("expiration_date")
        if expiration_date and expiration_date < date.today():
            raise serializers.ValidationError("Kartaning amal qilish muddati tugagan.")
        
        return super().validate(data)