from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password', 'is_courier', 'gender', 'birth_date')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get('email'),
            phone_number=validated_data.get('phone_number'),
            password=validated_data.get('password'),
            is_courier=validated_data.get('is_courier', False),
            gender=validated_data.get('gender'),
            birth_date=validated_data.get('birth_date')
        )
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
                return user
            raise serializers.ValidationError("Invalid login credentials.")
        raise serializers.ValidationError("Must include 'phone_number' and 'password'.")
