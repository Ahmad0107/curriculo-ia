# core/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

from core.models import Plano  # Removido RecursosPlano não utilizado


class CoreViewsTestCase(TestCase):
    """Testes para as views do core"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_home_view_exists(self):
        """Testa se a URL home existe"""
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 302])

    def test_planos_view_exists(self):
        """Testa se a URL planos existe"""
        response = self.client.get('/planos/')
        self.assertIn(response.status_code, [200, 302])

    def test_dashboard_view_exists(self):
        """Testa se a URL dashboard existe"""
        response = self.client.get('/dashboard/')
        self.assertIn(response.status_code, [200, 302, 403])  # 403 se requer login

    def test_exportar_cv_view_exists(self):
        """Testa se a URL exportar-cv existe"""
        response = self.client.get('/exportar-cv/')
        self.assertIn(response.status_code, [200, 302, 403])


class PlanoModelTestCase(TestCase):
    """Testes para o modelo Plano"""

    def setUp(self):
        self.plano = Plano.objects.create(
            nome='Plano Teste',
            preco=99.90,
            descricao='Plano de teste'
        )

    def test_plano_creation(self):
        """Testa se o plano foi criado corretamente"""
        self.assertEqual(self.plano.nome, 'Plano Teste')
        self.assertEqual(float(self.plano.preco), 99.90)

    def test_plano_str_representation(self):
        """Testa a representação em string do plano"""
        self.assertEqual(str(self.plano), 'Plano Teste')