from django.db import models

# Create your models here.


class Livro(models.Model):
    id_book = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    total_pag = models.IntegerField()
    id_user_cadFK = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    sinopse = models.TextField()
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome