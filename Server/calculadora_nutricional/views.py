from django.shortcuts import redirect, render
from .forms import RegistroForm, LoginForm
from .backend import MyBackend
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

MyBackend = MyBackend()

def index(request):
    return render(request, 'calculadora_nutricional/index.html')

def registro(request):
    if request.method == "POST":
        form = RegistroForm(data = request.POST)
        if form.is_valid():
            usuario = form.save(commit = False)
            usuario.save()
        return redirect('/registro')
    else:
        form = RegistroForm()
        return render(request,'calculadora_nutricional/registro.html', {"form": form})

def login(request, backend ='calculadora_nutricional.backend.MyBackend'):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['nombre_usuario']
            clave = form.cleaned_data['password_usuario']
            user = MyBackend.authenticate(request, username = usuario, password = clave)
            if user is not None:
                auth_login(request, user, backend)
        return render(request,'calculadora_nutricional/principal.html', {"user":user})
    else:
        form = LoginForm()
        return render(request,'calculadora_nutricional/ingreso.html', {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("/login")

@login_required(login_url="/login")
def principal(request):
    return render(request,'calculadora_nutricional/principal.html')