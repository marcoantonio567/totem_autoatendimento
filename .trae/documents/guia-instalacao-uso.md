# Guia de Instalação e Uso - Totem de Adoção Pet

## Requisitos do Sistema

### Software Necessário
- Python 3.9 ou superior
- Django 5.2.8
- SQLite (incluso com Python)
- pip (gerenciador de pacotes Python)

### Hardware Recomendado
- **Processador**: Intel i3 ou superior
- **Memória RAM**: 4GB mínimo
- **Armazenamento**: 10GB livres
- **Tela**: Touch screen 1920x1080 (recomendado para totem)
- **Sistema Operacional**: Windows 10/11, Linux ou macOS

## Instalação Passo a Passo

### 1. Preparação do Ambiente

```bash
# Verificar versão do Python
python --version
# ou
python3 --version

# Verificar versão do pip
pip --version
# ou
pip3 --version
```

### 2. Clonar/Extrair o Projeto

```bash
# Navegar até a pasta do projeto
cd c:\Users\2mbet\Desktop\totem_auto
```

### 3. Criar Ambiente Virtual (Recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 4. Instalar Dependências

```bash
# Instalar Django e outras dependências
pip install django==5.2.8

# Se for usar upload de imagens
pip install pillow
```

### 5. Configurar o Banco de Dados

```bash
# Aplicar migrações
python manage.py makemigrations
python manage.py migrate

# Criar superusuário (opcional, para admin)
python manage.py createsuperuser
```

### 6. Popular Banco com Dados de Teste

```bash
# Executar script de dados de teste
python criar_dados_teste.py
```

### 7. Configurar Arquivos Estáticos

```bash
# Coletar arquivos estáticos (opcional em desenvolvamento)
python manage.py collectstatic --noinput
```

### 8. Executar o Servidor

```bash
# Iniciar servidor de desenvolvamento
python manage.py runserver 0.0.0.0:8000

# Para produção, use um servidor WSGI como Gunicorn ou uWSGI
```

## Configuração para Produção

### Configurações do Django (settings.py)

```python
# Alterar para produção
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com', '192.168.1.100']

# Configurar banco de dados PostgreSQL (recomendado)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'totem_pet',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configurar email (opcional)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.seu-servidor.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@dominio.com'
EMAIL_HOST_PASSWORD = 'sua-senha'
```

### Configuração do Servidor Web

#### Apache com mod_wsgi
```apache
<VirtualHost *:80>
    ServerName seu-dominio.com
    
    WSGIScriptAlias / /caminho/para/totem_auto/totem/wsgi.py
    WSGIPythonHome /caminho/para/venv
    WSGIPythonPath /caminho/para/totem_auto
    
    <Directory /caminho/para/totem_auto/totem>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    
    Alias /static /caminho/para/totem_auto/static
    <Directory /caminho/para/totem_auto/static>
        Require all granted
    </Directory>
    
    Alias /media /caminho/para/totem_auto/media
    <Directory /caminho/para/totem_auto/media>
        Require all granted
    </Directory>
</VirtualHost>
```

#### Nginx com Gunicorn
```nginx
server {
    listen 80;
    server_name seu-dominio.com;
    
    location /static/ {
        alias /caminho/para/totem_auto/static/;
    }
    
    location /media/ {
        alias /caminho/para/totem_auto/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Uso do Sistema

### Como Usuário Final

1. **Iniciar**: Toque em "Começar Agora" na tela inicial
2. **Responder Perguntas**: Selecione suas preferências em cada etapa
3. **Ver Resultados**: Visualize pets compatíveis com sua busca
4. **Ver Detalhes**: Toque em "Ver Detalhes" para mais informações sobre um pet
5. **Demonstrar Interesse**: Toque em "Tenho Interesse na Adoção" se gostar de um pet

### Como Administrador

1. **Acessar Admin**: Navegue para `/admin/` e faça login
2. **Cadastrar Pets**: Use o formulário em "Cadastrar Pet" ou pelo admin
3. **Gerenciar Pets**: Edite informações, adicione fotos, marque como adotado
4. **Ver Estatísticas**: Acompanhe interações no painel administrativo

### Rotas Principais

| Rota | Descrição |
|------|-----------|
| `/` | Tela inicial do totem |
| `/pergunta/dupla/1/` | Primeira pergunta (tipo de pet) |
| `/pergunta/tripla/2/` | Segunda pergunta (porte) |
| `/pergunta/tripla/3/` | Terceira pergunta (idade) |
| `/pergunta/dupla/4/` | Quarta pergunta (tempo disponível) |
| `/resultados/` | Lista de pets recomendados |
| `/pet/<id>/` | Detalhes de um pet específico |
| `/cadastrar-pet/` | Formulário de cadastro de pet |
| `/admin/` | Interface administrativa Django |

## Manutenção

### Backup do Banco de Dados

```bash
# SQLite (desenvolvimento)
cp db.sqlite3 backup_$(date +%Y%m%d).sqlite3

# PostgreSQL (produção)
pg_dump totem_pet > backup_$(date +%Y%m%d).sql
```

### Logs e Monitoramento

```bash
# Ver logs do Django
tail -f logs/django.log

# Monitorar erros
grep -i error /var/log/apache2/error.log
```

### Atualização do Sistema

```bash
# Fazer backup antes de atualizar
cp -r totem_auto totem_auto_backup_$(date +%Y%m%d)

# Atualizar código
git pull origin main

# Aplicar migrações
python manage.py migrate

# Reiniciar servidor
sudo systemctl restart apache2  # ou nginx
```

## Solução de Problemas

### Problemas Comuns

#### 1. Erro de CSRF
**Solução**: Verificar configurações de CSRF no settings.py
```python
CSRF_TRUSTED_ORIGINS = ['http://seu-dominio.com', 'https://seu-dominio.com']
```

#### 2. Imagens não carregam
**Solução**: Verificar permissões de pasta
```bash
chmod 755 /caminho/para/totem_auto/media
chown www-data:www-data /caminho/para/totem_auto/media
```

#### 3. Servidor não inicia
**Solução**: Verificar portas e dependências
```bash
# Verificar se a porta está livre
netstat -tulpn | grep :8000

# Verificar dependências
pip check
```

#### 4. Erro de banco de dados
**Solução**: Verificar e aplicar migrações
```bash
python manage.py showmigrations
python manage.py migrate --fake-initial  # se necessário
```

## Suporte Técnico

### Informações de Contato
- **Email**: suporte@totempet.com
- **Telefone**: (11) 99999-9999
- **Horário**: Seg-Sex 9h-18h

### Documentação Adicional
- [Documento de Requisitos](prd-requisitos-totem-pet.md)
- [Documento de Arquitetura](arquitetura-tecnica-totem-pet.md)
- [Relatório de Fluxo](relatorio-fluxo-decisao.md)

### Comunidade
- **Fórum**: forum.totempet.com
- **GitHub**: github.com/totempet/totem-auto
- **Wiki**: wiki