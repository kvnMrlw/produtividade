from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as log
from django.contrib.auth.decorators import login_required

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render (request, 'cadastro.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        erros = {}

        if User.objects.filter(username=username).exists():
            erros['username'] = "Este nome de usuario já existe"

        if User.objects.filter(email=email).exists():
            erros['email'] = "Por favor adicione um email válido"

        if password != confirm_password:
            erros['password'] = "Insira uma senha válida"


        if erros:
            return render(request, "cadastro.html", {
                'erros': erros,
                'username': username,
                'email': email
            })

        User.objects.create_user(username=username, email=email, password=password)

        return redirect('/auth/login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            log(request, user)
            return redirect("plataforma")
        else:
            return render(request, "login.html", {
                'erro': "Usuario ou senha incorreto"
            })


@login_required
def plataforma(request):
    return HttpResponse("plataforma")