from django.db import models

# Create your models here.

class Perfil(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_userFK = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    descricao = models.TextField(blank=True)
    comentario = models.TextField(blank=True)
    arquivo = models.FileField(upload_to='perfis/', blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Perfil de {self.id_userFK}'