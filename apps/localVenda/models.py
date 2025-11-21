from django.db import models

# Create your models here.

class localVenda(models.Model):
    id_transacao = models.AutoField(primary_key=True)
    id_book_FK = models.ForeignKey('livro.Livro', on_delete=models.CASCADE)
    nome_livro = models.CharField(max_length=200)
    id_user_compFK = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='comprador')
    id_user_vendFK = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='vendedor')
    pagamento = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    previsao_ent = models.DateField()

    def __str__(self):
        return f"Transação {self.id_transacao}: {self.nome_livro} - {self.preco} BRL"