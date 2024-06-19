from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.views.generic import View
from django.shortcuts import render
from veiculo.models import Veiculo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculo.forms import FormularioVeiculo
from django.urls import reverse_lazy
from veiculo.serializers import SerializadorVeiculo
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


class ListarVeiculos(LoginRequiredMixin, ListView):
    """
    view para listar veículos
    """

    model = Veiculo
    context_object_name = 'veiculos'
    template_name ='veiculo/listar.html'
    queryset = Veiculo.objects.filter(modelo='F7');

    def get_queryset(self, **kwargs):
        queryset = Veiculo.objects.all()
        pesquisa = self.request.GET.get('pesquisa', None)
        if pesquisa is not None:
            queryset = queryset.filter(modelo__icontains=pesquisa)
        return queryset

class EditarVeiculos(LoginRequiredMixin, UpdateView):
    """
    View para edição de veiculos já cadastrados
    """

    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    """
    View para deletar veiculos já cadastrados
    """

    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')    
    

class CriarVeiculos(LoginRequiredMixin, CreateView):
    """
    View para a criação de novos veículos
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

    
class FotoVeiculo(View):
    """
    view para retornar as fotos dos veiculos
    """
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except Veiculo.DoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado!")
        except Exception as exception:
            raise exception
        
class APIListarVeiculos(ListAPIView):
    """
    View para listar as instâncias de veiculos por meio da API_REST
    """
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
    
class APIDeletarVeiculos(DestroyAPIView):    
    """
    View para deletar instâncias de veículos (por meio da API REST)    
    """
    serializer_class = SerializadorVeiculo  
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):        
        return Veiculo.objects.all()