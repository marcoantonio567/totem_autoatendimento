#!/usr/bin/env python
"""
Script para registrar pets específicos no banco de dados
Execute: python registrar_pets_especificos.py
"""

import os
import django
from django.conf import settings
from django.core.files import File
import shutil

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'totem.settings')
django.setup()

from app.models import Pet, PetImagem

def registrar_pets_especificos():
    """Registra pets específicos no banco de dados com suas imagens"""
    
    # Dados dos pets específicos
    pets_data = [
        {
            'nome': 'Gamora',
            'tipo': 'gato',
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 2,  # Estimativa baseada em "gatinha"
            'porte': 'pequeno',
            'personalidade': 'Muito brincalhona, ativa e cheia de energia. Adora brincar e explorar.',
            'descricao': 'Adote, gatinha castrada, vacinada, e microchipada. Muito brincalhona',
            'imagem_arquivo': 'Gamora.png'
        },
        {
            'nome': 'Luke',
            'tipo': 'cachorro',  # Inferido pelo nome e contexto
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 3,  # Estimativa
            'porte': 'medio',  # Estimativa
            'personalidade': 'Equilibrado, bem cuidado e sociável. Pronto para uma família amorosa.',
            'descricao': 'Castrado, vacinado, vermífugado, e microchipado',
            'imagem_arquivo': 'Luke.png'
        },
        {
            'nome': 'Davi',
            'tipo': 'gato',
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 1,  # "Gatinho" indica jovem
            'porte': 'pequeno',
            'personalidade': 'Jovem, curioso e carinhoso. Perfeito para adoção responsável.',
            'descricao': 'Gatinho para adoção responsável, castrado, vacinado, vermifugado e microchipado',
            'imagem_arquivo': 'davi.png'
        },
        {
            'nome': 'Dora',
            'tipo': 'gato',
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 4,  # "Adulta"
            'porte': 'pequeno',
            'personalidade': 'Madura, tranquila e carinhosa. Uma companheira ideal para quem busca estabilidade.',
            'descricao': 'Gatinha adulta, castrada, vacinada, vermifugada e microchipada.',
            'imagem_arquivo': 'Dora.png'
        },
        {
            'nome': 'Mavie',
            'tipo': 'cachorro',
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 5,  # "Adulto"
            'porte': 'medio',
            'personalidade': 'Adulto equilibrado, bem socializado e pronto para uma nova família.',
            'descricao': 'Adulto, castrado, vacinado e microchipado.',
            'imagem_arquivo': 'Mavie.png'
        },
        {
            'nome': 'Buck',
            'tipo': 'cachorro',
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 6,  # "Adulto"
            'porte': 'grande',  # Nome sugere porte maior
            'personalidade': 'Forte, leal e protetor. Um companheiro confiável para toda a família.',
            'descricao': 'Adulto, castrado, vacinado e microchipado.',
            'imagem_arquivo': 'Buck.png'
        },
        {
            'nome': 'Lady',
            'tipo': 'cachorro',
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 5,  # "Adulta"
            'porte': 'medio',
            'personalidade': 'Doce e carinhosa, mesmo com sua deficiência visual, é uma companheira especial e amorosa.',
            'descricao': 'Adulta, castrada, vacinado e microchipada. A Lady não enxerga de um olho.',
            'imagem_arquivo': 'Lady.png'
        },
        {
            'nome': 'Michelangelo',
            'tipo': 'gato',  # Nome artístico pode indicar gato
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 3,  # Estimativa
            'porte': 'pequeno',
            'personalidade': 'Artístico e elegante como seu nome sugere. Calmo e observador.',
            'descricao': 'Castrado, vacinado e microchipado.',
            'imagem_arquivo': 'Michelangelo.png'
        },
        {
            'nome': 'Verônica',
            'tipo': 'gato',
            'raca': 'SRD (Sem Raça Definida)',
            'idade': 4,  # "Adulta"
            'porte': 'pequeno',
            'personalidade': 'Adulta elegante e refinada. Uma companheira madura e carinhosa.',
            'descricao': 'Adulta, castrada, vacinada e microchipada.',
            'imagem_arquivo': 'Verônica.png'
        }
    ]
    
    # Caminho para as imagens
    imagens_path = r'c:\Users\VICTOR HUGO\Documents\Scripts\Projeto_totem\info-pets\Imagens'
    
    # Criar pets
    pets_criados = 0
    for pet_data in pets_data:
        # Extrair dados da imagem
        imagem_arquivo = pet_data.pop('imagem_arquivo')
        
        # Verificar se o pet já existe
        pet, created = Pet.objects.get_or_create(
            nome=pet_data['nome'],
            defaults=pet_data
        )
        
        if created:
            print(f"✅ Pet criado: {pet.nome}")
            pets_criados += 1
            
            # Adicionar imagem se o arquivo existir
            imagem_path = os.path.join(imagens_path, imagem_arquivo)
            if os.path.exists(imagem_path):
                try:
                    # Criar diretório media/pets se não existir
                    media_pets_dir = os.path.join(settings.MEDIA_ROOT, 'pets')
                    os.makedirs(media_pets_dir, exist_ok=True)
                    
                    # Copiar imagem para o diretório de media
                    nome_arquivo = f"{pet.nome.lower()}.png"
                    destino_path = os.path.join(media_pets_dir, nome_arquivo)
                    shutil.copy2(imagem_path, destino_path)
                    
                    # Criar registro da imagem no banco
                    pet_imagem = PetImagem.objects.create(
                        pet=pet,
                        imagem=f'pets/{nome_arquivo}',
                        principal=True
                    )
                    print(f"  📸 Imagem adicionada: {nome_arquivo}")
                    
                except Exception as e:
                    print(f"  ⚠️ Erro ao adicionar imagem para {pet.nome}: {e}")
            else:
                print(f"  ⚠️ Imagem não encontrada: {imagem_path}")
        else:
            print(f"ℹ️ Pet já existe: {pet.nome}")
    
    print(f"\n✅ Pets criados nesta execução: {pets_criados}")
    print(f"✅ Total de pets no banco: {Pet.objects.count()}")
    print("\nRegistro de pets específicos concluído com sucesso!")

if __name__ == "__main__":
    print("🚀 Registrando pets específicos...")
    print("📂 Verificando imagens disponíveis...")
    
    # Verificar se o diretório de imagens existe
    imagens_path = r'c:\Users\VICTOR HUGO\Documents\Scripts\Projeto_totem\info-pets\Imagens'
    if not os.path.exists(imagens_path):
        print(f"❌ Diretório de imagens não encontrado: {imagens_path}")
        exit(1)
    
    # Listar imagens disponíveis
    imagens_disponiveis = [f for f in os.listdir(imagens_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"📸 Imagens disponíveis: {', '.join(imagens_disponiveis)}")
    print()
    
    registrar_pets_especificos()