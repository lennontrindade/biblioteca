from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Aluguel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.CharField(max_length=100)  # Aqui você pode ajustar conforme seu modelo de Livros
    data_aluguel = models.DateTimeField(default=timezone.now)


def __str__(self):
    return f'{self.usuario.username} - {self.nome}'
