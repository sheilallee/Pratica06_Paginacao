from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Livro


def listar_livros(request):
    """
    View que lista os livros com paginação (10 livros por página).
    """
    # Obter todos os livros, ordenados por título
    livros_lista = Livro.objects.all().order_by('titulo')
    
    # Criar o paginator (10 livros por página)
    paginator = Paginator(livros_lista, 10)
    
    # Obter número da página do request
    numero_pagina = request.GET.get('page', 1)
    
    # Obter página específica
    livros = paginator.get_page(numero_pagina)
    
    # Passar para o template
    contexto = {
        'livros': livros,
        'paginator': paginator,
        'numero_pagina': numero_pagina,
    }
    
    return render(request, 'edu/listar_livros.html', contexto)
