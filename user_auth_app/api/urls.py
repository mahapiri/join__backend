from django.urls import path

from user_auth_app.api.views import CheckAuthVIew, UserCreateView, UserLoginView


urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('auth-check/', CheckAuthVIew.as_view()),
]