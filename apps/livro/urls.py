from django.urls import path
from .views import *

urlpatterns = [
    path("cadastrar/", cadastrar_livros, name="cadastrar_livro"),
    path("buscar/", buscar_livros, name="buscar_livros"),
    path("atualizar/", atualizar_livros, name="atualizar_livros"),
    path("deletar/", deletar_livros, name="deletar_livros"),
]
