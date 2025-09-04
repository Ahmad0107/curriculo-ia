# core/urls.py (alternativa com import absoluto)
from django.urls import path
from core import views  # ← Import absoluto

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('planos/', views.planos, name='planos'),
    path('exportar-cv/', views.exportar_cv, name='exportar_cv'),
]