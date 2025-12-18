from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from apps.livro.models import Livro
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@login_required
def cadastrar_livros(request):
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

@login_required
def buscar_livros(request):
    isbn = request.GET.get("isbn")

    if not isbn:
        return JsonResponse({"error": "ISBN não informado"}, status=400)
    
    try:
        livro = Livro.objects.get(isbn=isbn)
        return JsonResponse({
            "isbn": livro.isbn,
            "nome": livro.nome,
            "autor": livro.autor,
            "editora": livro.editora,
            "ano": livro.ano,
            "total_pag": livro.total_pag,
        })
    except Livro.DoesNotExist:
        return JsonResponse({"error": "Livro não encontrado"}, status=404)

@csrf_exempt
@login_required
def atualizar_livros(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        isbn = dados.get("isbn")

        if not isbn:
            return JsonResponse({"error": "ISBN não informado"}, status=400)

        try:
            livro = Livro.objects.get(isbn=isbn)
            livro.nome = dados.get("nome", livro.nome)
            livro.autor = dados.get("autor", livro.autor)
            livro.editora = dados.get("editora", livro.editora)
            livro.ano = dados.get("ano", livro.ano)
            livro.total_pag = dados.get("total_pag", livro.total_pag)
            livro.save()
            return JsonResponse({"status": "ok"})
        except Livro.DoesNotExist:
            return JsonResponse({"error": "Livro não encontrado"}, status=404)

    return JsonResponse({"error": "Método inválido"}, status=405)

@csrf_exempt
@login_required
def deletar_livros(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        isbn = dados.get("isbn")

        if not isbn:
            return JsonResponse({"error": "ISBN não informado"}, status=400)

        try:
            livro = Livro.objects.get(isbn=isbn)
            livro.delete()
            return JsonResponse({"status": "ok"})
        except Livro.DoesNotExist:
            return JsonResponse({"error": "Livro não encontrado"}, status=404)

    return JsonResponse({"error": "Método inválido"}, status=405)
