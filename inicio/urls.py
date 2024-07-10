from django.urls import path
from .views import index, imagem
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:fotos_id>/', imagem, name='imagem'),
    path('search/', views.search, name='search'),
]
