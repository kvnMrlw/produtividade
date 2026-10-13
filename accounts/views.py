from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render (request, 'cadastro.html', {'status': status})
    
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = User.objects.filter(username=username).first()
        if user:
            return redirect('/auth/cadastro/?status=0')

        if password != confirm_password:
            return redirect('/auth/cadastro/?status=2')

        user = User.objects.create_user(username=username, email=email, password=password)

        return redirect('/auth/login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == "POST":
        pass