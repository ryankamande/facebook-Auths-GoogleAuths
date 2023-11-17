from rest_framework import serializers, permissions, generics
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'password', 'username', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta(**validated_data)
            if password is not None:
                instance.set_password(password)
                instance.save()
            return instance


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name')



