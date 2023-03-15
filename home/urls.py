from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('diccionario/', views.diccionario, name='diccionario'),
    path('temas/', views.temas, name='temas'),
    path('juego/', views.juego, name='juego'),
]

