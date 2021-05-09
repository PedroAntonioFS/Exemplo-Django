from django.shortcuts import render, redirect, get_object_or_404

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
            form.save()
            return redirect('listar')
    else:
        form = CompraForm()
    return render(request, 'core/cadastrar.html', {'form': form})

def editar(request, pk):
    compra = get_object_or_404(Compra,id=pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'core/cadastrar.html', {'form': form})

