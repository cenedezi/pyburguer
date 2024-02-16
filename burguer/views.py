from django.shortcuts import render
from burguer.models import Produto


# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'buguer/home.html', context)

def produtos(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = {
        'produto': produto
    }
    return render(request, 'buguer/produto.html', context)