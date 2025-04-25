from django.urls import path

from contacts_app.api.views import contactView


urlpatterns = [
    path('', contactView)
]