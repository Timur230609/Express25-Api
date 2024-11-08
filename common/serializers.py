from rest_framework import serializers
from common.models import Address
from accaunt.models import User
from accaunt.serializers import RegisterSerializer

class AddressSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    class Meta:
        model = Address
        fields =  "__all__"
