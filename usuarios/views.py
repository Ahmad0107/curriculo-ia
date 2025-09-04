from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, UserProfileForm


def cadastro(request):
    """
    View para cadastro de novos usuários.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('core:dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})
def user_login(request):
    """
    View para login de usuários.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo de volta, {username}!')
                return redirect('core:dashboard')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


@login_required
def perfil(request):
    """
    View para edição do perfil do usuário.
    """
    if request.method == 'POST':
        # Verifica se é o formulário de perfil ou de senha
        if 'profile_submit' in request.POST:
            profile_form = UserProfileForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Perfil atualizado com sucesso!')
                return redirect('usuarios:perfil')
        elif 'password_submit' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Mantém o usuário logado
                messages.success(request, 'Senha alterada com sucesso!')
                return redirect('usuarios:perfil')
    else:
        profile_form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'usuarios/perfil.html', {
        'form': profile_form,
        'password_form': password_form
    })