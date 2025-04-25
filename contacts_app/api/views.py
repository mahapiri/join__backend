

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from contacts_app.api.serializer import ContactSerializer
from contacts_app.models import Contact


# View for listing all contacts, requiring login.
class ContactListView(LoginRequiredMixin, generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# View for retrieving, updating, or deleting a specific contact, requiring login.
class ContactDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# View for creating a new contact, requiring login.
class ContactCreateView(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = ContactSerializer
