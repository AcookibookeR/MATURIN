from django.urls import path
from . import views

urlpatterns = [
    path('paginainicial/', views.pagina, name='paginainicial'),
]