from django.shortcuts import render

# anuncio/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Anuncio
from .forms import AnuncioForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListarAnuncios(LoginRequiredMixin, ListView):
    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'

class CriarAnuncio(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')

class EditarAnuncio(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')

class DeletarAnuncio(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')