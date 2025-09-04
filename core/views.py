from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """
    View para a página inicial do site.
    """
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    """
    View para o dashboard do usuário após o login.
    """
    return render(request, 'core/dashboard.html')