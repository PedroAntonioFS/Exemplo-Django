from django.shortcuts import render

from .models import lista_de_compras
from .forms import lista_de_compra_form

# Create your views here.
def index(request):
    context = {
        "title" : "Página inicial",
        "msg" : "Hello World!"
    }

    return render(request, 'core/index.html', context)

def cadastrar(request):
    return render(request, 'core/cadastrar.html')

