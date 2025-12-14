from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage_view, name='frontpage'),
]