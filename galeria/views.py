from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia, Categoria
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        fotografias = Fotografia.objects.order_by("data_fotografia").filter(ativo=True)
        categorias = Categoria.objects.filter(ativo=True)
        return render(request, 'galeria\index.html', {"cards": fotografias, "tags": categorias, 'bootstrap': False})
    else:
        messages.error(request, 'Usuário não autenticado!')
        return redirect('login')


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia, 'bootstrap': False})    


def buscar(request):
    if request.user.is_authenticated:
        fotografias = Fotografia.objects.order_by("data_fotografia").filter(ativo=True)
        categorias = Categoria.objects.filter(ativo=True)
    
        if "buscar" in request.GET:
            nome_busca = request.GET['buscar']
            if nome_busca:
                fotografias = fotografias.filter(nome__icontains=nome_busca)

        return render(request, 'galeria/buscar.html', {"cards": fotografias, "tags": categorias, 'bootstrap': False})
    
    else:
        messages.error(request, 'Usuário não autenticado!')
        return redirect('login')
