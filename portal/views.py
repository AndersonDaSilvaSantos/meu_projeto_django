from django.shortcuts import render, redirect

from portal.forms import AutorForm
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

def autor_add(request):
    form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')

    context = {
        'form': form
    }

    return render(request,'portal/autor_add.html', context)

def autor_edit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(request.POST or None, instance=autor)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')

    context = {
        'form': form
    }

    return render(request,'portal/autor_edit.html', context)



def editora(request):
    return render(request, 'portal/editora.html')

def formato(request):
    return render(request, 'portal/formato.html')

def livro(request):
    return render(request, 'portal/livro.html')