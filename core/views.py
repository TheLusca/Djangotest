from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):
    print(dir(request.user))
    print(f'User:{request.user}')
    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        estado = 'Usuário nao logado'
    else:
        estado = 'Usuário logado'

    context = {
        'curso': 'Programação web com django framework',
        'outro': 'Django é massa!',
        'logado': estado,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    print(f'PK: {pk}')
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }

    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charsert=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charsert=utf8', status=500)
