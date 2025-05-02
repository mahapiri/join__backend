"""
URL configuration for join project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', homeView),
    path('tasks/', include('tasks_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/tasks/', include('tasks_app.api.urls')),
    path('api/contacts/', include('contacts_app.api.urls')),    
    path('api/users/', include('join.api.urls')),    
]
