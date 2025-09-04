# core/admin.py
from django.contrib import admin
from core.models import Experiencia, Educacao, Habilidade, Plano, RecursosPlano, Curriculo

# Registre todos os modelos
admin.site.register(Experiencia)
admin.site.register(Educacao)
admin.site.register(Habilidade)
admin.site.register(Plano)
admin.site.register(RecursosPlano)
admin.site.register(Curriculo)