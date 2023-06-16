from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class FormularioPedido(forms.Form):
    nombre = forms.CharField(
        required=True,
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'input-box','placeholder':'Nombre '})
        )
    apellido = forms.CharField(
        required=True,
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'input-box','placeholder':'Apellido'})
        )
   
    calle = forms.CharField(
        required=True,
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'input-box flex','placeholder':'Calle'})
        )
    numero = forms.IntegerField(
        required=True,
        label='',
        max_value=6000,
        widget=forms.TextInput(attrs={'class':'input-box flex','placeholder':'Número'}))
    tarjeta = forms.IntegerField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={'class':'input-box flex','placeholder':'0000111122223333'}))
    cvv = forms.IntegerField(
        required=True,
        label='',
        max_value=999,
        widget=forms.TextInput(attrs={'class':'input-box flex','placeholder':'000'}))
   