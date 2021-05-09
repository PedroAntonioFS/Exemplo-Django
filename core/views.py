from django.shortcuts import render, redirect

from .models import Compra
from .forms import CompraForm

# Create your views here.
def index(request):
    context = {
        "title" : "Página inicial",
        "msg" : "Hello World!"
    }

    return render(request, 'core/index.html', context)

def listar(request):
    lista = Compra.objects.all()
    return render(request, 'core/listar.html', {'lista': lista})

def cadastrar(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.save()
            return redirect('listar')
    else:
        form = CompraForm()
    return render(request, 'core/cadastrar.html', {'form': form})

