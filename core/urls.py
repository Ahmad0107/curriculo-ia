from django.urls import path
from . import views

app_name = 'core'  # Namespace para as URLs

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard



]