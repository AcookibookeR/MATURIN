from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def frontpage_view(request):
    if request.method == "POST":
        action = request.POST.get("action")

        username = request.POST.get("username")
        password = request.POST.get("password")

        if action == "login":
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("perfil")
            else:
                messages.error(request, "Usuário ou senha inválidos")

        elif action == "register":
            email = request.POST.get("email")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Usuário já existe")
            else:
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                messages.success(request, "Cadastro realizado com sucesso")
                return redirect("frontpage")

    return render(request, "frontpage/index.html")