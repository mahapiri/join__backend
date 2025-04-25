from django.urls import path

from contacts_app.api.views import ContactCreateView, ContactDetailView, ContactListView


urlpatterns = [
    path('', ContactListView.as_view()),
    path('<int:pk>/', ContactDetailView.as_view()),
    path('create/', ContactCreateView.as_view()),
]