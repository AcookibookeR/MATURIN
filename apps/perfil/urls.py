from django.urls import path
from .views import *

urlpatterns = [
    path("", perfil_view, name='perfil'),
    path("usuario/cadastrar/", cadastrar_usuario, name="cadastrar_usuario"),
]