from django.urls import path
from .views import (
    TarefaListView, 
    TarefaDetailView, 
    TarefaCreateView, 
    TarefaUpdateView, 
    TarefaDeleteView
)

urlpatterns = [
    path('', TarefaListView.as_view(), name='lista_tarefas'),
    path('<int:pk>/', TarefaDetailView.as_view(), name='detalhe_tarefa'),
    path('criar/', TarefaCreateView.as_view(), name='criar_tarefa'),
    path('<int:pk>/atualizar/', TarefaUpdateView.as_view(), name='atualizar_tarefa'),
    path('<int:pk>/deletar/', TarefaDeleteView.as_view(), name='deletar_tarefa'),
]
