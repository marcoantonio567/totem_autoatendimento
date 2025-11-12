# app/urls.py
from django.urls import path
from . import views # Assuming you have a views.py

urlpatterns = [
    # Example pattern
    path('', views.tela_base, name='tela base'), 
    path('', views.tela_comecar, name='comecar'), 
    path('pergunta_dupla/', views.pergunta_dupla, name='pergunta_dupla'),
    path('pergunta_tripla/', views.pergunta_tripla, name='pergunta_tripla'),
    path('pet_detalhes/', views.pet_detalhes, name='pet_detalhes'),
    path('pet_lista/', views.pet_lista, name='pet_lista'),
]