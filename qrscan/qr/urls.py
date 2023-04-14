from django.contrib import admin
from django.urls import path, include
from .views import home, logging, usuarios
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', logging, name='bienvenido'),
    path('accounts/login/bienvenido/', home, name='welcome'),
    path('accounts/logout/home/', logging, name='goodbye'),
    path("accounts/", include("django.contrib.auth.urls")),
]

