from django import forms
from django.db.models import fields
from .models import Registro, Contacto

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('rut','nombre','apellido','email','genero', 'edad', 'password')

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','apellido','email', 'mensaje')

class LoginForm(forms.Form):
    nombre_usuario = forms.CharField(widget=forms.TextInput)
    password_usuario = forms.CharField(widget=forms.PasswordInput)
