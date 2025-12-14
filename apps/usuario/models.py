from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nome = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
