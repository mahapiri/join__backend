

from rest_framework import generics
from contacts_app.api.serializer import ContactSerializer
from contacts_app.models import Contact


# View for listing all contacts.
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# View for retrieving, updating, or deleting a specific contact.
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# View for creating a new contact.
class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer
