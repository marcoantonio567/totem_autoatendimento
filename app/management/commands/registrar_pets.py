#!/usr/bin/env python
"""
Comando Django para registrar pets específicos
"""

from django.core.management.base import BaseCommand
from django.conf import settings
from app.models import Pet, PetImagem
import os
import shutil

class Command(BaseCommand):
    help = 'Registra pets específicos no banco de dados'

    def handle(self, *args, **options):
        """Registra pets específicos no banco de dados com suas imagens"""
        
        self.stdout.write("🚀 Registrando pets específicos...")
        
        # Dados dos pets específicos
        pets_data = [
            {
                'nome': 'Gamora',
                'tipo': 'gato',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 2,
                'porte': 'pequeno',
                'personalidade': 'Muito brincalhona, ativa e cheia de energia. Adora brincar e explorar.',
                'descricao': 'Adote, gatinha castrada, vacinada, e microchipada. Muito brincalhona',
                'imagem_arquivo': 'Gamora.png'
            },
            {
                'nome': 'Luke',
                'tipo': 'cachorro',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 3,
                'porte': 'medio',
                'personalidade': 'Equilibrado, bem cuidado e sociável. Pronto para uma família amorosa.',
                'descricao': 'Castrado, vacinado, vermífugado, e microchipado',
                'imagem_arquivo': 'Luke.png'
            },
            {
                'nome': 'Davi',
                'tipo': 'gato',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 1,
                'porte': 'pequeno',
                'personalidade': 'Jovem, curioso e carinhoso. Perfeito para adoção responsável.',
                'descricao': 'Gatinho para adoção responsável, castrado, vacinado, vermifugado e microchipado',
                'imagem_arquivo': 'davi.png'
            },
            {
                'nome': 'Dora',
                'tipo': 'gato',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 4,
                'porte': 'pequeno',
                'personalidade': 'Madura, tranquila e carinhosa. Uma companheira ideal para quem busca estabilidade.',
                'descricao': 'Gatinha adulta, castrada, vacinada, vermifugada e microchipada.',
                'imagem_arquivo': 'Dora.png'
            },
            {
                'nome': 'Mavie',
                'tipo': 'cachorro',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 5,
                'porte': 'medio',
                'personalidade': 'Adulto equilibrado, bem socializado e pronto para uma nova família.',
                'descricao': 'Adulto, castrado, vacinado e microchipado.',
                'imagem_arquivo': 'Mavie.png'
            },
            {
                'nome': 'Buck',
                'tipo': 'cachorro',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 6,
                'porte': 'grande',
                'personalidade': 'Forte, leal e protetor. Um companheiro confiável para toda a família.',
                'descricao': 'Adulto, castrado, vacinado e microchipado.',
                'imagem_arquivo': 'Buck.png'
            },
            {
                'nome': 'Lady',
                'tipo': 'cachorro',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 5,
                'porte': 'medio',
                'personalidade': 'Doce e carinhosa, mesmo com sua deficiência visual, é uma companheira especial e amorosa.',
                'descricao': 'Adulta, castrada, vacinado e microchipada. A Lady não enxerga de um olho.',
                'imagem_arquivo': 'Lady.png'
            },
            {
                'nome': 'Michelangelo',
                'tipo': 'gato',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 3,
                'porte': 'pequeno',
                'personalidade': 'Artístico e elegante como seu nome sugere. Calmo e observador.',
                'descricao': 'Castrado, vacinado e microchipado.',
                'imagem_arquivo': 'Michelangelo.png'
            },
            {
                'nome': 'Verônica',
                'tipo': 'gato',
                'raca': 'SRD (Sem Raça Definida)',
                'idade': 4,
                'porte': 'pequeno',
                'personalidade': 'Adulta elegante e refinada. Uma companheira madura e carinhosa.',
                'descricao': 'Adulta, castrada, vacinada e microchipada.',
                'imagem_arquivo': 'Verônica.png'
            }
        ]
        
        # Caminho para as imagens
        imagens_path = os.path.join(settings.BASE_DIR, 'info-pets', 'Imagens')
        
        if not os.path.exists(imagens_path):
            self.stdout.write(
                self.style.ERROR(f"❌ Diretório de imagens não encontrado: {imagens_path}")
            )
            return
        
        # Listar imagens disponíveis
        imagens_disponiveis = [f for f in os.listdir(imagens_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.stdout.write(f"📸 Imagens disponíveis: {', '.join(imagens_disponiveis)}")
        
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
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Pet criado: {pet.nome}")
                )
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
                        self.stdout.write(f"  📸 Imagem adicionada: {nome_arquivo}")
                        
                    except Exception as e:
                        self.stdout.write(
                            self.style.WARNING(f"  ⚠️ Erro ao adicionar imagem para {pet.nome}: {e}")
                        )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"  ⚠️ Imagem não encontrada: {imagem_path}")
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f"ℹ️ Pet já existe: {pet.nome}")
                )
        
        self.stdout.write(
            self.style.SUCCESS(f"\n✅ Pets criados nesta execução: {pets_criados}")
        )
        self.stdout.write(
            self.style.SUCCESS(f"✅ Total de pets no banco: {Pet.objects.count()}")
        )
        self.stdout.write(
            self.style.SUCCESS("Registro de pets específicos concluído com sucesso!")
        )