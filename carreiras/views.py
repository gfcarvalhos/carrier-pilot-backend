from carreiras.models import Atividade, Recomendacao, Progresso
from carreiras.serializers import AtividadeSerializer, RecomendacaoSerializer, ProgressoSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class AtividadeViewSet(viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de atividades.

  Métodos HTTP Permitidos:
  - GET, PUT
  """
  queryset= Atividade.objects.all().order_by('id')
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['categoria', 'prioridade']
  filterset_fields = ['titulo', 'categoria', 'prioridade']
  serializer_class=AtividadeSerializer
  http_method_names = ["get", "put"]

class RecomendacaoViewSet(viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de Recomendacao.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Recomendacao.objects.all().order_by('id')
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['usuario__nome', 'usuario__data_cadastro', 'status', 'data_gerada']
  filterset_fields = ['usuario__nome', 'usuario__email', 'status']
  serializer_class=RecomendacaoSerializer

class ProgressoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de Progresso.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Progresso.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario__nome', 'usuario__data_cadastro', 'data_concluida', 'status']
    filterset_fields = ['usuario__nome', 'usuario__email', 'status', 'data_concluida']
    serializer_class = ProgressoSerializer