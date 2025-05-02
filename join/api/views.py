from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import generics

from join.api.serializer import UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        try:
            user = serializer.save()
            return user
        except IntegrityError as e:
            raise IntegrityError(f"Fehler beim Erstellen des Benutzers: {str(e)}")
