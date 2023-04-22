from django.contrib import admin
from django.urls import path, include
from .views import index, logging, qrnuevo


urlpatterns = [
    path('', logging, name='bienvenido'),
    path('accounts/login/bienvenido/', index, name='welcome'),
    path('accounts/logout/home/', logging, name='goodbye'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('qrnuevo/', qrnuevo)
]
