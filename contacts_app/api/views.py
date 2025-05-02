

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import generics
from contacts_app.api.serializer import ContactSerializer
from contacts_app.models import Contact


# View for listing all contacts, requiring login.
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# View for retrieving, updating, or deleting a specific contact, requiring login.
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# View for creating a new contact, requiring login.
class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer