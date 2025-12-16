from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from apps.livro.models import Livro
# Create your views here.

@login_required
def cadastrar_livro(request):
    if request.method == "POST":
        dados = json.loads(request.body)

        Livro.objects.update_or_create(
            isbn=dados.get("isbn"),
            defaults={
                "isbn": dados.get("isbn", ""),
                "nome": dados.get("nome", ""),
                "autor": dados.get("autor", ""),
                "editora": dados.get("editora", ""),
                "ano": dados.get("ano", ""),
                "total_pag": dados.get("total_pag", ""),
            }
        )
        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "Método inválido"}, status=405)