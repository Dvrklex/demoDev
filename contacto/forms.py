from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField()
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
   