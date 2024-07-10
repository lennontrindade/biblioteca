# Create your models here.
from django.db import models


class Fotos(models.Model):
    OPCOES_GENERO = [
        ('LITERATURA BRASILEIRA', 'literatura brasileira'),
        ('MANGÁ', 'mangá'),
        ('FICÇAO CIENTÍFICA', 'ficçao científica'),
        ('TERROR', ' terror'),
        ('ROMANCE', 'romance'),
        ('POESIA', 'poesia'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    ano = models.CharField(max_length=15, null=False, blank=False)
    descricao = models.TextField(max_length=2000, null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%y/%m/%d', blank=True)
    genero = models.CharField(max_length=50, choices=OPCOES_GENERO, null=True, blank=True)

    def __str__(self):
        return f'Foto [nome={self.nome}]'
