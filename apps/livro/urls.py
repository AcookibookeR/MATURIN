from django.urls import path
from .views import *

urlpatterns = [
    path("cadastrar/", cadastrar_livro, name="cadastrar_livro"),
]