from django.db import models

# Create your models here.


class Livro(models.Model):
    id_book = models.AutoField(primary_key=True)
    isbn = models.IntegerField()
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editora = models.CharField(max_length=200)
    ano = models.IntegerField()
    total_pag = models.IntegerField()
    
    def __str__(self):
        return self.nome