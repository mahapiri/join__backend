from django.urls import path

from join.api.views import UserCreateView, UserLoginView


urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('login/', UserLoginView.as_view()),
]
