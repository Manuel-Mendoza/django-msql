from django.contrib import admin
from django.urls import path
from blogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('generales/', Generales, name='generales'),
    path('programacion/', Programacion, name='programacion'),
    path('juegos/', Juegos, name='juegos'),
    path('contactos/', Contactos, name='contactos'),
    path('<slug:slug>/', DetallePost, name='post'),
]
