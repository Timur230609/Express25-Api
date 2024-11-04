from rest_framework import serializers
from common.models import Address
from accaunt.models import User

class AddressSerializer(serializers.ModelSerializer):
    # user = Userserializer()  vazifa
    class Meta:
        model = Address
        fields =  "__all__"
