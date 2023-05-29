from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class ViewRegistro(View):
    
    
    def get(self,request):
        form = UserCreationForm()
        return render(request,'autenticacion/registro.html',{"form":form})
    
    def post(self,request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            
            return redirect('Home')
        else: 
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,'autenticacion/registro.html',{"form":form})
        
        
def login_view(request):
    return render(request,'autenticacion/login.html')