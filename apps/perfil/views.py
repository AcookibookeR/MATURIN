from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from apps.usuario.models import Usuario
# Create your views here.

@login_required
def perfil_view(request):
    perfil = request.user.usuario

    if not perfil.nome or not perfil.telefone:
        return render(request, "perfil/index.html")
    
    return render(request, "perfil/gerenciamento.html", {"perfil": perfil})


@login_required
def cadastrar_usuario(request):
    if request.method == "POST":
        dados = json.loads(request.body)

        Usuario.objects.update_or_create(
            user=request.user,
            defaults={
                "nome": dados.get("nome", ""),
                "endereco": dados.get("endereco", ""),
                "telefone": dados.get("telefone", ""),
            }
        )

        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "Método inválido"}, status=405)