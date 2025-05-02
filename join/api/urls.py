from django.urls import path

from join.api.views import UserCreateView


urlpatterns = [
    path('create/', UserCreateView.as_view()),
]
