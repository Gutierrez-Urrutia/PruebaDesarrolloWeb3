import re
from django import forms
from .models import Cliente
from django.core.exceptions import ValidationError

class FormCliente(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmar Contraseña")
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'rut',
            'username',
            'telefono',
            'direccion',
            'pais',
            'region',
            'comuna',
            'password',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su rut sin puntos y con guión'}),
            'username': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'usuario@correo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dirección'}),
            'pais' : forms.Select(attrs={'class': 'form-control', 'id': 'pais'}), 
            'region' : forms.Select(attrs={'class': 'form-control', 'id': 'region', 'disabled': 'true'}),
            'comuna' : forms.Select(attrs={'class': 'form-control', 'id': 'comuna', 'disabled': 'true'}),
        }

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'username': 'Correo Electrónico',
            'telefono': 'Teléfono Móvil',
            'direccion': 'Dirección',
            'pais': 'País',
            'region': 'Región',
            'comuna': 'Comuna',
        }
    
    def __init__(self, *args, **kwargs):
        super(FormCliente, self).__init__(*args, **kwargs)
        self.fields['pais'].required = True
        self.fields['pais'].error_messages = {'required': 'Por favor, seleccione un país.'}
        self.fields['region'].required = True
        self.fields['region'].error_messages = {'required': 'Por favor, seleccione una región.'}
        self.fields['comuna'].required = True
        self.fields['comuna'].error_messages = {'required': 'Por favor seleccione una comuna.'}

    def clean_email(self):
        email = self.cleaned_data['username']
        if Cliente.objects.filter(username=username).exists():
            raise ValidationError("El correo electrónico ya está registrado.")
        return email     

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        pattern = r'^\d{6,8}-[\dKk]$'
        if not re.match(pattern, rut):
            raise ValidationError("Ingrese rut sin puntos y con guión")
        elif Cliente.objects.filter(rut=rut).exists():
            raise ValidationError("El rut ya está registrado.")
        return rut    

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        pattern = r'^\+569\d{8}$'
        if not re.match(pattern, telefono):
            raise ValidationError("Ingrese un número con formato +56912345678")
        return telefono 
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        if password != repassword:
            self.add_error('password', "Las contraseñas no coinciden")
        return cleaned_data