from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from pyexpat.errors import messages
from .models import Aluguel
from inicio.models import Fotos
from .forms import FiltroGeneroForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')  # Redirecione para a página desejada após o registro
    else:
        form = UserCreationForm()
    return render(request, 'inicio/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')  # Redirecione para a página desejada após o login
    else:
        form = AuthenticationForm()
    return render(request, 'inicio/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')  # Redirecione para a página desejada após o logout


def livros_alugados(request):
    alugueis = Aluguel.objects.filter(usuario=request.user)
    return render(request, 'inicio/livros_alugados.html', {'alugueis': alugueis})


def reservar_livro(request, foto_id):
    foto = get_object_or_404(Fotos, pk=foto_id)
    if request.method == 'POST':
        # Crie um registro de Aluguel para o usuário logado e o livro selecionado
        Aluguel.objects.create(usuario=request.user, livro=foto.nome)
        return redirect('livros_alugados')  # Redirecione para a página de livros alugados

    return render(request, 'inicio/livros_alugados.html', {'foto': foto})


def lista_livros(request):
    fotos = Fotos.objects.all()  # Query inicial para todos os livros

    # Processar o formulário de filtro se for um POST
    if request.method == 'POST':
        form = FiltroGeneroForm(request.POST)
        if form.is_valid():
            genero_selecionado = form.cleaned_data.get('genero')
            if genero_selecionado:
                fotos = Fotos.objects.filter(genero=genero_selecionado)
    else:
        form = FiltroGeneroForm()

    context = {
        'form': form,
        'fotos': fotos,
    }
    return render(request, 'inicio/lista_livros.html', context)
