#!/usr/bin/env python
"""
Script para criar dados de teste no banco de dados
Execute: python criar_dados_teste.py
"""

import os
import django
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'totem.settings')
django.setup()

from app.models import Pet, PetImagem

def criar_pets_teste():
    """Cria pets de teste no banco de dados"""
    
    # Dados de teste
    pets_data = [
        {
            'nome': 'Rex',
            'tipo': 'cachorro',
            'raca': 'Golden Retriever',
            'idade': 3,
            'porte': 'grande',
            'personalidade': 'Muito brincalhão, carinhoso, adora crianças e é super sociável. Perfeito para famílias.',
            'descricao': 'Rex é um golden retriever de 3 anos que adora brincar e receber carinho. É muito dócil e se dá bem com crianças e outros pets. Está castrado e com todas as vacinas em dia.'
        },
        {
            'nome': 'Luna',
            'tipo': 'gato',
            'raca': 'Siamês',
            'idade': 2,
            'porte': 'pequeno',
            'personalidade': 'Calma, independente, mas muito carinhosa quando se sente confortável.',
            'descricao': 'Luna é uma gata siamesa elegante e tranquila. Gosta de lugares altos e momentos de paz, mas adora um carinho no colo. É castrada e educada.'
        },
        {
            'nome': 'Thor',
            'tipo': 'cachorro',
            'raca': 'Beagle',
            'idade': 1,
            'porte': 'medio',
            'personalidade': 'Energético, curioso, adora farejar e explorar. Muito brincalhão.',
            'descricao': 'Thor é um beagle jovem cheio de energia. Precisa de espaço para correr e brincar. É muito inteligente e aprende comandos rapidamente.'
        },
        {
            'nome': 'Mel',
            'tipo': 'gato',
            'raca': 'Persa',
            'idade': 4,
            'porte': 'medio',
            'personalidade': 'Muito calma, preguiçosa, adora dormir e receber carinhos.',
            'descricao': 'Mel é uma gata persa dócil e tranquila. Prefere ambientes calmos e não gosta muito de barulho. É perfeita para apartamentos e pessoas que buscam um pet mais quieto.'
        },
        {
            'nome': 'Max',
            'tipo': 'cachorro',
            'raca': 'Labrador',
            'idade': 5,
            'porte': 'grande',
            'personalidade': 'Sociável, inteligente, protetor e muito leal à família.',
            'descricao': 'Max é um labrador experiente e muito equilibrado. É ótimo com crianças e se adapta bem a diferentes ambientes. Está castrado e com saúde perfeita.'
        },
        {
            'nome': 'Nina',
            'tipo': 'gato',
            'raca': 'Maine Coon',
            'idade': 3,
            'porte': 'grande',
            'personalidade': 'Brincalhona, sociável, gosta de água e é muito carinhosa.',
            'descricao': 'Nina é uma maine coon impressionante pelo tamanho e personalidade. É muito sociável e até gosta de brincar com água. Perfeita para famílias ativas.'
        },
        {
            'nome': 'Buddy',
            'tipo': 'cachorro',
            'raca': 'Shih Tzu',
            'idade': 6,
            'porte': 'pequeno',
            'personalidade': 'Carinhoso, companheiro, adora colo e é muito leal.',
            'descricao': 'Buddy é um shih tzu de porte pequeno, perfeito para apartamentos. Adora ficar no colo e é muito companheiro. É ideal para idosos ou pessoas que buscam um pet calmo.'
        },
        {
            'nome': 'Sophie',
            'tipo': 'gato',
            'raca': 'Angorá',
            'idade': 1,
            'porte': 'pequeno',
            'personalidade': 'Ativa, curiosa, brincalhona e muito carinhosa.',
            'descricao': 'Sophie é uma gata jovem cheia de energia. Adora brincar com brinquedos e explorar lugares novos. É muito carinhosa e se adapta bem a ambientes com outros pets.'
        }
    ]
    
    # Criar pets
    for pet_data in pets_data:
        pet, created = Pet.objects.get_or_create(
            nome=pet_data['nome'],
            defaults=pet_data
        )
        
        if created:
            print(f"✅ Pet criado: {pet.nome}")
        else:
            print(f"ℹ️ Pet já existe: {pet.nome}")
    
    print(f"\n✅ Total de pets no banco: {Pet.objects.count()}")
    print("\nDados de teste criados com sucesso!")

if __name__ == "__main__":
    print("🚀 Criando dados de teste...")
    criar_pets_teste()