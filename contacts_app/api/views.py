

from rest_framework import generics
from contacts_app.api.serializer import ContactSerializer
from contacts_app.models import Contact


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer