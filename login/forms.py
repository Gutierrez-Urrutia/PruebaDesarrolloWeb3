from django import forms
from django.core.exceptions import ValidationError
from registro.models import Cliente
from django.contrib.auth import authenticate

class FormLogin(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}), label="Correo Electrónico", )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}), label="Contraseña",)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if not Cliente.objects.filter(username=username).exists():
            raise ValidationError('El correo electrónico no está registrado.')
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Las credenciales son incorrectas.')
        
        self.user = user

        return cleaned_data
    
