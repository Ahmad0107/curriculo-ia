# core/models.py
from django.db import models
from django.contrib.auth.models import User


class Experiencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"


class Educacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.curso} - {self.instituicao}"


class Habilidade(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField()

    def __str__(self):
        return self.nome


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class RecursosPlano(models.Model):
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    recurso = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.plano.nome} - {self.recurso}"


class Curriculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='curriculos/')
    nome_original = models.CharField(max_length=255)
    data_upload = models.DateTimeField(auto_now_add=True)
    compatibilidade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.nome_original}"