from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# View simples para cadastro
def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('usuarios/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('usuarios/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/cadastro/', cadastro_view, name='cadastro'),  # ← URL DE CADASTRO
]