from django.contrib.auth.models import User
from rest_framework import serializers
from contacts_app.models import Contact


# Serializer for managing contact data associated with tasks.
class ContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Contact
        fields = ['id', 'linked_user', 'name', 'email', 'phone', 'initial', 'color']
