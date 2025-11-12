from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_comecar, name='tela_comecar'),
    path('comecar/', views.tela_comecar, name='comecar'),
    path('pergunta/dupla/<int:step>/', views.pergunta_dupla, name='pergunta_dupla'),
    path('pergunta/tripla/<int:step>/', views.pergunta_tripla, name='pergunta_tripla'),
    path('salvar-preferencia/', views.salvar_preferencia, name='salvar_preferencia'),
    path('resultados/', views.resultados, name='resultados'),
    path('pet/<int:pet_id>/', views.pet_detalhes, name='pet_detalhes'),
    path('cadastrar-pet/', views.cadastrar_pet, name='cadastrar_pet'),
    path('base/', views.tela_base, name='tela_base'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
]