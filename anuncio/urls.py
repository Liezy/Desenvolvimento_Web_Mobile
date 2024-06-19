# anuncio/urls.py
from django.urls import path
from .views import ListarAnuncios, CriarAnuncio, EditarAnuncio, DeletarAnuncio

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncio.as_view(), name='criar-anuncio'),
    path('<int:pk>/editar/', EditarAnuncio.as_view(), name='editar-anuncio'),
    path('<int:pk>/deletar/', DeletarAnuncio.as_view(), name='deletar-anuncio'),
]
