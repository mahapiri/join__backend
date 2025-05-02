from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True} 
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        validated_data['username'] = email

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'].title(),
            last_name=validated_data['last_name'].title(),
            email=email
        )
        return user