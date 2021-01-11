from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account
from django import forms


class CreateUserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Las contraseñas no son iguales",
    }

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Usuario',
                    'required': 'True'
                }),
            'email':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo',
                    'required': 'True'
                }),
        }

        error_messages = {
            'username': {
                "unique": "El usuario ya existe",
                'required': "El usuario es obligatorio",
                'invalid': "El usuario es inválido",
            },
            'email': {
                "unique": "El correo ya existe",
                'required': "El correo es obligatorio",
                'invalid': "El correo es inválido",
            },
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': 'True'
            })
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repite la contraseña',
                'required': 'True'
            })
