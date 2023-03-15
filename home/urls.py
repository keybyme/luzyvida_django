from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('diccionario/', views.diccionario, name='diccionario'),
    path('temas/', views.temas, name='temas'),
]

