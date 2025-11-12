from django.shortcuts import render



# Create your views here.
def tela_base(request):
    return render(request, 'base.html', {})

def footer(request):
    return render(request, 'footer.html', {})

def header(request):
    return render(request, 'header.html', {})

def tela_comecar(request):
    return render(request, 'comecar.html', {})

def pergunta_dupla(request):
    return render(request, 'pergunta_dupla.html', {})

def pergunta_tripla(request):
    return render(request, 'pergunta_tripla.html', {})

def pet_detalhes(request):
    return render(request, 'pet_detalhes.html', {})

def pet_lista(request):
    return render(request, 'pet_lista.html', {})