from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarefa

# R (Read - Lista)
class TarefaListView(ListView):
    model = Tarefa
    context_object_name = 'tarefas' # Nome da variável no template

# R (Read - Detalhe)
class TarefaDetailView(DetailView):
    model = Tarefa
    context_object_name = 'tarefa'

# C (Create - Criar)
class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'completa']
    success_url = reverse_lazy('lista_tarefas') # Redireciona após sucesso

# U (Update - Atualizar)
class TarefaUpdateView(UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'completa']
    success_url = reverse_lazy('lista_tarefas')

# D (Delete - Excluir)
class TarefaDeleteView(DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    success_url = reverse_lazy('lista_tarefas')
