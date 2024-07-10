from django.contrib import admin
from inicio.models import Fotos


# Register your models here.

class Listafotos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'autor', 'ano')
    list_filter = ('genero',)
    list_display_links = ('id', 'nome', 'autor', 'ano')


admin.site.register(Fotos, Listafotos)
