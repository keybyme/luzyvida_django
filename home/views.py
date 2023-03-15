from django.shortcuts import render
from .models import Diccionario, Ltema
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home/home.html')

def diccionario(request):
    dicc_list = Diccionario.objects.all()
    #set up pagination
    p = Paginator(dicc_list, 12)
    page = request.GET.get('page')
    data_pages = p.get_page(page)
    context = {
        'data_pages':data_pages,
        'title':'Diccionario',
    }
    return render(request, 'home/diccionario.html', context)

def temas(request):
    temas_list = Ltema.objects.all()
    #set up pagination
    p = Paginator(temas_list, 12)
    page = request.GET.get('page')
    data_pages = p.get_page(page)
    context = {
        'data_pages':data_pages,
        'title':'Temas',
    }
    return render(request, 'home/temas.html', context)