from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    """
    Formulário personalizado para criação de usuários com campos adicionais.
    """
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'Email'
    }))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'Nome'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'Sobrenome'
    }))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza os widgets dos campos padrão
        self.fields['username'].widget.attrs.update({
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'placeholder': 'Nome de usuário'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'placeholder': 'Senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'placeholder': 'Confirmação de senha'
        })

class UserProfileForm(forms.ModelForm):
    """
    Formulário para edição do perfil do usuário.
    """
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'Telefone'
    }))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'Breve descrição sobre você',
        'rows': 3
    }))
    country = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'País'
    }))
    state = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'Estado'
    }))
    city = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        'placeholder': 'Cidade'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'bio', 'country', 'state', 'city']