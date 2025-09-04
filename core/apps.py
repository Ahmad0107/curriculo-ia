from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuração do aplicativo Core.

    Define o nome do aplicativo e o nome amigável para exibição
    no painel administrativo do Django.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Núcleo do Sistema'