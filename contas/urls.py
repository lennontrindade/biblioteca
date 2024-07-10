# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reservar/<int:foto_id>/', views.reservar_livro, name='reservar_livro'),
    path('filtro-livros/', views.lista_livros, name='filtro_livros'),
    path('livros_alugados/', views.livros_alugados, name='livros_alugados'),

]
