from django.db import models
from django.contrib.auth.models import User


class Plano(models.Model):
    """
    Modelo para representar os planos de assinatura disponíveis.

    Atributos:
        nome (str): Nome do plano (Gratuito, Básico, Premium)
        preco_mensal (Decimal): Preço mensal do plano
        preco_anual (Decimal): Preço anual com desconto
        descricao (str): Descrição das características do plano
        recursos (str): Lista de recursos separados por vírgula
        ativo (bool): Se o plano está disponível para contratação
        criado_em (datetime): Data de criação do registro
        atualizado_em (datetime): Data da última atualização
    """
    nome = models.CharField(max_length=100)
    preco_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    preco_anual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descricao = models.TextField()
    recursos = models.TextField(help_text="Lista de recursos separados por vírgula")
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        ordering = ['preco_mensal']


class RecursosPlano(models.Model):
    """
    Modelo para gerenciar recursos dos planos de forma flexível.

    Permite associar recursos específicos a cada tipo de plano.
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    disponivel_gratis = models.BooleanField(default=False)
    disponivel_basico = models.BooleanField(default=False)
    disponivel_premium = models.BooleanField(default=False)
    icone = models.CharField(max_length=50, default='fas fa-check',
                             help_text="Classe do FontAwesome para o ícone")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Recurso de Plano'
        verbose_name_plural = 'Recursos de Planos'


class Contato(models.Model):
    """
    Modelo para armazenar mensagens de contato dos usuários.
    """
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    lido = models.BooleanField(default=False)
    respondido = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'
        ordering = ['-criado_em']