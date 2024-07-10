from django.shortcuts import render, get_list_or_404
from .models import Fotos


# Create your views here.
def index(request):
    fotos = Fotos.objects.all()
    return render(request, 'inicio/index.html', {'cards': fotos})


def imagem(request, fotos_id):
    foto = get_list_or_404(Fotos, pk=fotos_id)
    return render(request, 'inicio/imagem.html', {'foto': foto})


def search(request):
    query = request.GET.get('search')
    if query:
        results = Fotos.objects.filter(nome__icontains=query)
    else:
        results = Fotos.objects.none()
    return render(request, 'inicio/resultados.html', {'query': query, 'results': results})
