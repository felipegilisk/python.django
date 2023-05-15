from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia, Categoria


def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(ativo=True)
    categorias = Categoria.objects.filter(ativo=True)
    return render(request, 'galeria\index.html', {"cards": fotografias, "tags": categorias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})    


def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(ativo=True)
    categorias = Categoria.objects.filter(ativo=True)
    
    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)

    return render(request, 'galeria/buscar.html', {"cards": fotografias, "tags": categorias})
