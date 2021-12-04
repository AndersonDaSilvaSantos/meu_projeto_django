from django.shortcuts import render

from portal.models import Autor


def home(request):
    return render(request, 'portal/home.html')

def dashboard(request):
    return render(request, 'portal/dashbord.html')

def autor(request):
    autores = Autor.objects.all()

    context = {
        'autores': autores
    }
    return render(request, 'portal/autor.html', context)

def editora(request):
    return render(request, 'portal/editora.html')

def formato(request):
    return render(request, 'portal/formato.html')

def livro(request):
    return render(request, 'portal/livro.html')