#!/usr/bin/env python
"""
Script de teste para verificar configuração do Django
"""

import os
import sys

print("🔍 Verificando ambiente...")
print(f"Python: {sys.version}")
print(f"Diretório atual: {os.getcwd()}")

try:
    import django
    print(f"✅ Django importado: versão {django.get_version()}")
except ImportError as e:
    print(f"❌ Erro ao importar Django: {e}")
    sys.exit(1)

# Configurar Django
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'totem.settings')
    django.setup()
    print("✅ Django configurado com sucesso")
except Exception as e:
    print(f"❌ Erro ao configurar Django: {e}")
    sys.exit(1)

try:
    from app.models import Pet, PetImagem
    print("✅ Modelos importados com sucesso")
except Exception as e:
    print(f"❌ Erro ao importar modelos: {e}")
    sys.exit(1)

# Testar conexão com o banco
try:
    total_pets = Pet.objects.count()
    print(f"✅ Conexão com banco OK. Pets existentes: {total_pets}")
except Exception as e:
    print(f"❌ Erro ao conectar com banco: {e}")
    sys.exit(1)

print("\n🎉 Ambiente configurado corretamente!")