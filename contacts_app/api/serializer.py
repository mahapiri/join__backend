from rest_framework import serializers
from contacts_app.models import Contact


# Serializer for the Contact model to handle serialization and deserialization.
class ContactSerializer(serializers.ModelSerializer):
    initial = serializers.CharField(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
