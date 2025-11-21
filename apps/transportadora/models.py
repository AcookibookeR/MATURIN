from django.db import models

# Create your models here.

class Transportadora(models.Model):
    id_transportadora = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome
