from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователей"""

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Ваш логин",
            "class": "input_form"})
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Ваш Email",
            "class": "input_form"})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "input_form",
            "placeholder": 'Ваш пароль'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "input_form",
            "placeholder": "Повторите пароль"})
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class AuthorizationForm(AuthenticationForm):
    '''Форма авторизации пользователей'''

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input_form',
            'placeholder': 'Ваш логин'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input_form',
            'placeholder': 'Ваш пароль'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')

