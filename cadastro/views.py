from django.shortcuts import render
from django.db.models.functions import Lower
from .models import Pessoas

# Create your views here.

def index(request):
    pessoa_id = request.GET.get('id')
    if pessoa_id:
         pessoa = Pessoas.objects.get(id=pessoa_id)
         return render(request, 'cadastro/index.html', {'pessoa':pessoa, 'acao': 'Editar'})
    else:
        return render(request, 'cadastro/index.html', {'acao': 'Cadastrar'})

def listagem(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    idade = request.POST.get('idade')
    nascimento = request.POST.get('dnascimento')
    email = request.POST.get('email')
    apelido = request.POST.get('apelido')
    obs = request.POST.get('obs')
    
    pessoa_id = request.POST.get('pessoa_id')
    
    if(pessoa_id):
        pessoa = Pessoas.objects.get(id=pessoa_id)
        pessoa.nome = nome
        pessoa.sobrenome = sobrenome
        pessoa.idade = idade
        pessoa.nascimento = nascimento
        pessoa.email = email
        pessoa.apelido = apelido
        pessoa.obs = obs
        pessoa.save()
    else:
        pessoas = Pessoas.objects.create(nome=nome, sobrenome = sobrenome, idade=idade, nascimento = nascimento, email = email, apelido = apelido, obs = obs)
    
    pessoas = Pessoas.objects.all().order_by(Lower('nome'), Lower('sobrenome'))
    
    return render(request, 'cadastro/listagem.html', {'pessoas': pessoas})