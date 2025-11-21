from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    reputacao = models.DecimalField(max_digits=3, decimal_places=2)
    telefone = models.CharField(max_length=15)
    e_vendedor = models.BooleanField(default=False)
    senha = models.CharField(max_length=50)
    id_user = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome