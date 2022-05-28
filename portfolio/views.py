#  hello/views.py
from django.shortcuts import render
import datetime
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse

from django.http import HttpResponseRedirect

from django.shortcuts import render

from .forms import PublicacaoForm

from .models import Cadeira
from .models import Escola
from .models import Projeto
from .models import Publicacao


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def escolas_page_view(request):
    context = {'escolas': Escola.objects.all()}
    return render(request, 'portfolio/escolas.html', context)


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def blog_page_view(request):
    context = {'publicacoes': Publicacao.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def nova_publicacao_page_view(request):
    form = PublicacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'form': form}
    return render(request, 'portfolio/nova_publicacao.html', context)


def editar_publicacao_page_view(request, publicacao_id):
    publicacao = Publicacao.objects.get(id=publicacao_id)
    form = PublicacaoForm(request.POST or None, instance=publicacao)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'publicacao_id': publicacao_id}
    return render(request, 'portfolio/editar_publicacao.html', context)


def apagar_publicacao_page_view(request, publicacao_id):
    Publicacao.objects.get(id=publicacao_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def login_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, "portfolio/login.html", {
                'message': "Credenciais Inválidas."
            })
    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)
    return render(request, 'portfolio/home.html', {
        "message": "Logged out."
    })


def quiz_view_page(request):
    return render(request, 'portfolio/quiz.html')
