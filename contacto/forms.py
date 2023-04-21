from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class FormularioContacto(forms.Form):
    nombre = forms.CharField(
        required=True,
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'input-box','placeholder':'Nombre '})
        )
    email = forms.EmailField(
        required=True,
        label='',
        max_length=50,
        validators=[EmailValidator(message='Ingrese un dirección de correo válida')],
        widget=forms.TextInput(attrs={'class':'input-box','placeholder':'Dirección email'})
        )
    asunto = forms.CharField(
        required=True,
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'input-box','placeholder':'Asunto'})
        )
    mensaje = forms.CharField(
        required=True,
        label='',
        max_length=1000,
        widget=forms.Textarea(attrs={'class':'input-box message-box','placeholder':'Escriba su mensaje aquí...'}))
   