#!/usr/bin/env python
"""
Script de execução automática do sistema Totem de Adoção Pet
Execute este script para configurar e iniciar o sistema
"""

import os
import subprocess
import sys
from pathlib import Path

def executar_comando(comando, descricao):
    """Executa um comando e retorna o resultado"""
    print(f"\n🔧 {descricao}...")
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"✅ Sucesso: {descricao}")
            return True
        else:
            print(f"❌ Erro: {descricao}")
            print(f"Detalhes: {resultado.stderr}")
            return False
    except Exception as e:
        print(f"❌ Erro ao executar: {descricao}")
        print(f"Exceção: {str(e)}")
        return False

def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    print("📋 Verificando dependências...")
    
    # Verificar Python
    try:
        resultado = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print(f"✅ Python: {resultado.stdout.strip()}")
    except:
        print("❌ Python não encontrado")
        return False
    
    # Verificar Django
    try:
        import django
        print(f"✅ Django: {django.VERSION}")
    except ImportError:
        print("❌ Django não encontrado. Instalando...")
        return executar_comando(f"{sys.executable} -m pip install django==5.2.8", "Instalando Django")
    
    # Verificar Pillow (para imagens)
    try:
        import PIL
        print("✅ Pillow: Instalado")
    except ImportError:
        print("❌ Pillow não encontrado. Instalando...")
        return executar_comando(f"{sys.executable} -m pip install pillow", "Instalando Pillow")
    
    return True

def configurar_banco():
    """Configura o banco de dados"""
    print("\n🗄️ Configurando banco de dados...")
    
    # Aplicar migrações
    if not executar_comando(f"{sys.executable} manage.py makemigrations", "Criando migrações"):
        return False
    
    if not executar_comando(f"{sys.executable} manage.py migrate", "Aplicando migrações"):
        return False
    
    return True

def criar_dados_teste():
    """Cria dados de teste"""
    print("\n🧪 Criando dados de teste...")
    
    if os.path.exists("criar_dados_teste.py"):
        return executar_comando(f"{sys.executable} criar_dados_teste.py", "Criando dados de teste")
    else:
        print("⚠️ Script de dados de teste não encontrado")
        return True

def iniciar_servidor():
    """Inicia o servidor Django"""
    print("\n🚀 Iniciando servidor...")
    print("\n" + "="*50)
    print("🎯 SISTEMA TOTEM DE ADOÇÃO PET")
    print("="*50)
    print("\n📍 URLs do sistema:")
    print("   • Tela Inicial: http://localhost:8000/")
    print("   • Admin Django: http://localhost:8000/admin/")
    print("\n⚡ Pressione Ctrl+C para parar o servidor")
    print("="*50 + "\n")
    
    # Iniciar servidor
    os.system(f"{sys.executable} manage.py runserver 0.0.0.0:8000")

def main():
    """Função principal"""
    print("\n" + "="*60)
    print("🐕 SISTEMA TOTEM DE ADOÇÃO PET - CONFIGURAÇÃO AUTOMÁTICA")
    print("="*60)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("manage.py"):
        print("❌ Erro: Este script deve ser executado no diretório raiz do projeto")
        print("   Certifique-se de estar na pasta que contém o arquivo manage.py")
        return
    
    # Configurar variável de ambiente Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'totem.settings')
    
    # Executar passos de configuração
    passos = [
        ("Verificando dependências", verificar_dependencias),
        ("Configurando banco de dados", configurar_banco),
        ("Criando dados de teste", criar_dados_teste),
    ]
    
    for descricao, funcao in passos:
        print(f"\n{'='*20} {descricao} {'='*20}")
        if not funcao():
            print(f"\n❌ Configuração interrompida em: {descricao}")
            print("   Por favor, corrija os erros acima e tente novamente.")
            return
    
    # Iniciar servidor
    iniciar_servidor()

if __name__ == "__main__":
    main()