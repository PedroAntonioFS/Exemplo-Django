from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        "title" : "Página inicial",
        "msg" : "Hello World!"
    }

    return render(request, 'core/index.html', context)

