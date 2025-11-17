from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Pet, PetImagem
import json

def calcular_compatibilidade(pet, preferencias):
    """Calcula a compatibilidade entre um pet e as preferências do usuário"""
    pontuacao = 0
    
    # Tipo de pet (0-40 pontos)
    tipo_preferido = preferencias.get('tipo')
    if tipo_preferido and tipo_preferido != 'sem_preferencia':
        if pet.tipo == tipo_preferido:
            pontuacao += 40
    else:
        pontuacao += 20
    
    # Porte (0-25 pontos)
    porte_compatibilidade = {
        'pequeno': {'pequeno': 25, 'medio': 15, 'grande': 5},
        'medio': {'pequeno': 15, 'medio': 25, 'grande': 15},
        'grande': {'pequeno': 5, 'medio': 15, 'grande': 25}
    }
    
    preferencia_porte = preferencias.get('porte')
    if preferencia_porte and preferencia_porte != 'sem_preferencia':
        pontuacao += porte_compatibilidade.get(preferencia_porte, {}).get(pet.porte, 0)
    else:
        pontuacao += 20  # Pontuação média se não houver preferência
    
    # Idade (0-20 pontos)
    idade_preferida = preferencias.get('idade')
    if idade_preferida and idade_preferida != 'sem_preferencia':
        if pet.idade_categoria == idade_preferida:
            pontuacao += 20
    else:
        pontuacao += 10  # Pontuação média se não houver preferência
    
    # Personalidade (0-15 pontos)
    personalidade_preferida = preferencias.get('personalidade', [])
    if personalidade_preferida and 'sem_preferencia' not in personalidade_preferida:
        for palavra in personalidade_preferida:
            if palavra.lower() in pet.personalidade.lower():
                pontuacao += 5
    else:
        pontuacao += 7  # Pontuação média se não houver preferência
    
    return min(pontuacao, 100)

# Views principais
def tela_base(request):
    return render(request, 'base.html', {})

def header(request):
    return render(request, 'header.html', {})

def footer(request):
    return render(request, 'footer.html', {})

def tela_comecar(request):
    """Tela inicial com botão para começar o fluxo"""
    return render(request, 'comecar.html', {})

def pergunta_dupla(request, step=1):
    """Perguntas com duas opções"""
    perguntas = {
        1: {
            'titulo': 'Você prefere um cachorro ou um gato?',
            'opcoes': [
                {'valor': 'cachorro', 'texto': 'Cachorro', 'icone': '🐕'},
                {'valor': 'gato', 'texto': 'Gato', 'icone': '🐈'}
            ],
            'proxima': '/pergunta/dupla/2/'
        },
        2: {
            'titulo': 'Você prefere macho ou fêmea?',
            'opcoes': [
                {'valor': 'macho', 'texto': 'Macho', 'icone': '🐾'},
                {'valor': 'femea', 'texto': 'Fêmea', 'icone': '🐾'}
            ],
            'proxima': '/pergunta/dupla/3/'
        },
        3: {
            'titulo': 'Qual faixa etária você prefere?',
            'opcoes': [
                {'valor': 'filhote', 'texto': 'Filhote (0-2 anos)', 'icone': '🍼'},
                {'valor': 'adulto', 'texto': 'Adulto (3-7 anos)', 'icone': '🐕'}
            ],
            'proxima': '/pergunta/tripla/4/'
        }
    }
    
    pergunta = perguntas.get(step)
    if not pergunta:
        return redirect('tela_comecar')
    
    return render(request, 'pergunta_dupla.html', {
        'pergunta': pergunta,
        'step': step
    })

def pergunta_tripla(request, step=2):
    """Perguntas com três opções"""
    perguntas = {
        4: {
            'titulo': 'Qual porte você prefere?',
            'opcoes': [
                {'valor': 'pequeno', 'texto': 'Pequeno', 'icone': '🐭'},
                {'valor': 'medio', 'texto': 'Médio', 'icone': '🐕'},
                {'valor': 'grande', 'texto': 'Grande', 'icone': '🐺'}
            ],
            'proxima': '/resultados/'
        }
    }
    
    pergunta = perguntas.get(step)
    if not pergunta:
        return redirect('tela_comecar')
    
    return render(request, 'pergunta_tripla.html', {
        'pergunta': pergunta,
        'step': step
    })

def salvar_preferencia(request):
    """Salva as preferências do usuário na sessão"""
    if request.method == 'POST':
        data = json.loads(request.body)
        chave = data.get('chave')
        valor = data.get('valor')
        
        if 'preferencias' not in request.session:
            request.session['preferencias'] = {}
        
        request.session['preferencias'][chave] = valor
        request.session.modified = True
        
        return JsonResponse({'status': 'sucesso'})
    return JsonResponse({'status': 'erro'}, status=400)

def resultados(request):
    """Mostra pets compatíveis com as preferências"""
    preferencias = request.session.get('preferencias', {})
    
    # Buscar pets disponíveis
    pets_disponiveis = Pet.objects.filter(disponivel=True)
    
    # Calcular compatibilidade
    pets_compatíveis = []
    for pet in pets_disponiveis:
        compatibilidade = calcular_compatibilidade(pet, preferencias)
        if compatibilidade >= 50:  # Mostrar apenas pets com 50%+ compatibilidade
            pets_compatíveis.append({
                'pet': pet,
                'compatibilidade': compatibilidade
            })
    
    # Ordenar por compatibilidade
    pets_compatíveis.sort(key=lambda x: x['compatibilidade'], reverse=True)
    
    return render(request, 'pet_lista.html', {
        'pets_compatíveis': pets_compatíveis,
        'preferencias': preferencias
    })

def pet_detalhes(request, pet_id):
    """Mostra detalhes de um pet específico"""
    pet = get_object_or_404(Pet, id=pet_id)
    imagens = pet.imagens.all()
    
    return render(request, 'pet_detalhes.html', {
        'pet': pet,
        'imagens': imagens
    })

def cadastrar_pet(request):
    """Formulário para cadastrar novo pet"""
    if request.method == 'POST':
        try:
            pet = Pet.objects.create(
                nome=request.POST.get('nome'),
                tipo=request.POST.get('tipo'),
                raca=request.POST.get('raca'),
                idade=int(request.POST.get('idade')),
                porte=request.POST.get('porte'),
                personalidade=request.POST.get('personalidade'),
                descricao=request.POST.get('descricao', ''),
                disponivel=True
            )
            
            # Salvar imagens
            if request.FILES.get('imagem'):
                PetImagem.objects.create(
                    pet=pet,
                    imagem=request.FILES.get('imagem'),
                    principal=True
                )
            
            messages.success(request, 'Pet cadastrado com sucesso!')
            return redirect('pet_detalhes', pet_id=pet.id)
            
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar pet: {str(e)}')
    
    return render(request, 'cadastrar_pet.html', {})

def painel_pets(request):
    q = request.GET.get('q', '').strip()
    filtro_disponivel = request.GET.get('disponivel')
    pets = Pet.objects.all()
    if q:
        pets = pets.filter(nome__icontains=q)
    if filtro_disponivel in ['true', 'false']:
        pets = pets.filter(disponivel=(filtro_disponivel == 'true'))
    pets = pets.order_by('nome')
    return render(request, 'painel_pets.html', {'pets': pets, 'q': q, 'filtro_disponivel': filtro_disponivel})

def editar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        try:
            pet.nome = request.POST.get('nome')
            pet.tipo = request.POST.get('tipo')
            pet.raca = request.POST.get('raca')
            pet.idade = int(request.POST.get('idade'))
            pet.porte = request.POST.get('porte')
            pet.personalidade = request.POST.get('personalidade')
            pet.descricao = request.POST.get('descricao', '')
            pet.save()
            if request.FILES.get('imagem'):
                PetImagem.objects.create(pet=pet, imagem=request.FILES.get('imagem'), principal=not pet.imagens.exists())
            messages.success(request, 'Pet atualizado com sucesso!')
            return redirect('painel_pets')
        except Exception as e:
            messages.error(request, f'Erro ao atualizar pet: {str(e)}')
    imagens = pet.imagens.all()
    return render(request, 'editar_pet.html', {'pet': pet, 'imagens': imagens})

def excluir_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        nome = pet.nome
        pet.delete()
        messages.success(request, f'Pet "{nome}" excluído com sucesso!')
        return redirect('painel_pets')
    return redirect('painel_pets')

def alternar_disponibilidade_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    pet.disponivel = not pet.disponivel
    pet.save()
    messages.success(request, 'Disponibilidade atualizada!')
    return redirect('painel_pets')