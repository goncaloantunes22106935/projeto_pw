#  hello/views.py
from django.shortcuts import render
import datetime

from django.contrib.auth import authenticate, login, logout

from django.urls import reverse

from django.http import HttpResponseRedirect

from django.shortcuts import render

from .forms import PublicacaoForm
from .forms import TcfForm
from .forms import QuizzForm

from .models import Cadeira
from .models import Escola
from .models import Projeto
from .models import Publicacao
from .models import Final_Project
from .models import Quizz
from .models import Tecnologia


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


def projetos_finais_page_view(request):
    context = {'projetos_finais': Final_Project.objects.all()}
    return render(request, 'portfolio/projetos_finais.html', context)


def novo_tcf_page_view(request):
    form = TcfForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tcf'))
    context = {'form': form}
    return render(request, 'portfolio/novo_tcf.html', context)


def editar_tcf_page_view(request, tcf_id):
    tcf = Final_Project.objects.get(id=tcf_id)
    form = TcfForm(request.POST or None, instance=tcf)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tcf'))

    context = {'form': form, 'tcf_id': tcf_id}
    return render(request, 'portfolio/editar_tcf.html', context)


def apagar_tcf_page_view(request, tcf_id):
    Final_Project.objects.get(id=tcf_id).delete()
    return HttpResponseRedirect(reverse('portfolio:tcf'))


def quizz_resultado(request):
    pontuacao = 0
    curso = request.POST.get('curso')
    linguagens = request.POST.get('linguagens')

    if curso == 'informatica':
        pontuacao += 15
    if linguagens == 'javascript':
        pontuacao += 15

    return pontuacao


def quiz_view_page(request):
    quizz = Quizz.objects.all()
    context = {'quizz': quizz}

    if request.method == 'POST':
        n = request.POST.get('nome')
        a = request.POST.get('email')
        p = quizz_resultado(request)
        r = Quizz(nome=n, email=a, pontuacao=p)
        r.save()

    return render(request, 'portfolio/quiz.html', context)


def api_page_view(request):
    return render(request, 'portfolio/api_page.html')


def site_page_view(request):
    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request, 'portfolio/Site.html', context)
