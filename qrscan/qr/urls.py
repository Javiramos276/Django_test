from django.contrib import admin
from django.urls import path, include
from .views import home, logging, usuarios

urlpatterns = [
    path('', logging, name='bienvenido'),
    path("accounts/logout", logging, name='logout'),
    path('accounts/login/bienvenido/', home, name='welcome'),
    path('accounts/logout/home/', logging, name='goodbye'),
    path('accounts/login/', usuarios)
]