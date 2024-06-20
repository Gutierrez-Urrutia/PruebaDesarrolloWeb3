from django import forms
from .models import Cliente

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'rut',
            'email',
            'telefono',
            'direccion',
            'pais',
            'region',
            'comuna',
            'password',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'pais': 'País',
            'region': 'Región',
            'comuna': 'Comuna',
            'password': 'Contraseña',
        }