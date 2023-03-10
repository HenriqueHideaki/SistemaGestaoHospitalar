from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .forms import FuncaoForm
from .models import Funcao
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'core/base.html')

def lista_funcoes(request):
    form = FuncaoForm
    funcoes_list = Funcao.objects.all().order_by('nome')
    paginator = Paginator(funcoes_list, 2)
    page = request.GET.get('page')
    funcoes = paginator.get_page(page)
    data = {}
    data['funcao'] = funcoes
    data['form'] = form
    return render(request, 'core/lista_funcoes.html',{
        'form': form,
        'funcoes': funcoes,
    })


def funcao_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Funcao.objects.filter(nome=nome).count()
        
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este nome !')
            return redirect('funcao_novo')
        else:
            form = FuncaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_funcoes')
    else:
        form = FuncaoForm
        return render( request, 'core/funcao_novo.html', {
            'form': form
            
        })
    
def funcao_update(request, id):

    funcao = Funcao.objects.get(id=id)
    form = FuncaoForm(request.POST)
    data = {}
    data['funcao'] = funcao
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_funcoes')
    else:
        form = FuncaoForm
        return render( request, 'core/funcao_update.html', data)
    
def funcao_search(request):
    search = request.GET.get('search')
    funcoes = Funcao.objects.filter(nome__icontains=search)
    form = FuncaoForm()
    data = {}
    data['funcoes'] = funcoes
    data['form'] = form
    return render(request, 'core/lista_funcoes.html', data)


def funcao_delete(request, id):
    funcao = Funcao.objects.get(id=id)
    funcao.delete()
    messages.success(request, 'Registro excluido com sucesso')
    return redirect('lista_funcoes')

# def funcao_delete(request, id):
#     if request.method == 'POST':
#         funcao = get_object_or_404(Funcao, id=id)
#         funcao.delete()
#         return redirect('funcao_delete')
#     else:
#         return render(request, 'core/funcao_delete.html')