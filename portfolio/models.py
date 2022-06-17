from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Professor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_do_professor = models.CharField(max_length=50)
    pagina_do_linkedin = models.CharField(max_length=150, default="https://www.linkedin.com/login/pt")
    pagina_da_lusofona = models.CharField(max_length=150, default="https://www.ulusofona.pt/")

    def __str__(self):
        return self.nome_do_professor


class Pessoa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_da_pessoa = models.CharField(max_length=50)
    pagina_do_linkedin = models.CharField(max_length=150, default="https://www.linkedin.com/login/pt")
    pagina_do_github = models.CharField(max_length=150, default="https://www.ulusofona.pt/")

    def __str__(self):
        return self.nome_da_pessoa


class Cadeira(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_da_cadeira = models.CharField(max_length=50)
    ano_da_cadeira = models.IntegerField(default=1)
    semestre_da_cadeira = models.IntegerField(default=1)
    ects = models.IntegerField(default=6)
    link_da_pagina = models.CharField(max_length=150)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    estrelas_da_cadeira = models.IntegerField(default=3)

    def __str__(self):
        return self.nome_da_cadeira


class Competencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_da_competencia = models.CharField(max_length=50)
    descricao_curta_da_competencia = models.CharField(max_length=200)
    disciplina_onde_foi_trabalhada_a_competencia = models.ForeignKey(Cadeira, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome_da_competencia


class Projeto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_do_projeto = models.CharField(max_length=50)
    descricao_do_projeto = models.CharField(max_length=500)
    ano_de_realizacao_do_projeto = models.IntegerField(default=2022)
    cadeira_do_projeto = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    link_do_github = models.CharField(max_length=100, default="https://github.com/goncaloantunes22106935")
    link_do_youtube = models.CharField(max_length=100, default="https://www.youtube.com/")
    tecnologias_usadas = models.CharField(max_length=150, default="Nenhuma tecnologia utilizada.")
    aptidao_utilizada = models.ForeignKey(Competencia, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_do_projeto


class Escola(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_da_escola = models.CharField(max_length=150)
    curso_frequentado = models.CharField(max_length=50, blank=True)
    local_da_escola = models.CharField(max_length=50)
    quantos_anos_estive = models.IntegerField(default=1)
    grau_de_ensino = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_da_escola


class Publicacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    autor_da_publicacao = models.CharField(max_length=50)
    data_da_publicacao = models.DateField
    titulo_da_publicacao = models.CharField(max_length=50)
    descricao = models.CharField(max_length=700)
    link_do_github = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.titulo_da_publicacao


class Jogador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_do_jogador = models.CharField(max_length=50)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_do_jogador


class Final_Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    autor = models.CharField(max_length=50)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.IntegerField(default=2021)
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(max_length=700)
    relatorio = models.CharField(max_length=100, blank=True)
    link_github = models.CharField(max_length=150, default="https://github.com/goncaloantunes22106935")
    video_demonstrativo = models.CharField(max_length=150, default="https://www.youtube.com/")

    def __str__(self):
        return self.titulo


class Quizz(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    criador = models.CharField(max_length=50)
    descricao = models.CharField(max_length=700)
    pagina = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

