from django import forms
from django.core.exceptions import ValidationError
from registro.models import Cliente
from django.contrib.auth import authenticate

class FormLogin(forms.Form):
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        labels = {
            'username': 'Nombre de usuario:',
            'password': 'Contraseña:'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

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
