from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Plano, RecursosPlano


class CoreViewsTestCase(TestCase):
    """
    Testes para as views do app core.
    """

    def setUp(self):
        """Configuração inicial para os testes."""
        self.client = Client()

        # Criar usuário para testes que requerem login
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )

        # Criar planos para testes
        self.plano_gratis = Plano.objects.create(
            nome='Grátis',
            preco_mensal=0,
            descricao='Plano gratuito',
            recursos='Upload de currículo, 1 análise por mês',
            ativo=True
        )

        # Criar recursos para testes
        self.recurso1 = RecursosPlano.objects.create(
            nome='Upload de CV',
            descricao='Permite fazer upload do currículo',
            disponivel_gratis=True,
            disponivel_basico=True,
            disponivel_premium=True
        )

    def test_home_view_status_code(self):
        """Testa se a view home retorna status code 200."""
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        """Testa se a view home usa o template correto."""
        response = self.client.get(reverse('core:home'))
        self.assertTemplateUsed(response, 'core/home.html')

    def test_dashboard_view_requires_login(self):
        """Testa se a view dashboard requer autenticação."""
        response = self.client.get(reverse('core:dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirecionamento para login

    def test_dashboard_view_authenticated(self):
        """Testa se a view dashboard funciona para usuários autenticados."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('core:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')

    def test_planos_view(self):
        """Testa se a view planos retorna os planos corretamente."""
        response = self.client.get(reverse('core:planos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grátis')
        self.assertTemplateUsed(response, 'core/planos.html')


class PlanoModelTestCase(TestCase):
    """Testes para o modelo Plano."""

    def test_plano_creation(self):
        """Testa a criação de um plano."""
        plano = Plano.objects.create(
            nome='Teste',
            preco_mensal=99.90,
            descricao='Plano de teste',
            recursos='Recurso1, Recurso2',
            ativo=True
        )
        self.assertEqual(plano.nome, 'Teste')
        self.assertEqual(plano.preco_mensal, 99.90)
        self.assertTrue(plano.ativo)

    def test_plano_str_representation(self):
        """Testa a representação em string do modelo Plano."""
        plano = Plano.objects.create(
            nome='Premium',
            preco_mensal=99.90,
            descricao='Plano premium',
            recursos='Todos os recursos',
            ativo=True
        )
        self.assertEqual(str(plano), 'Premium')