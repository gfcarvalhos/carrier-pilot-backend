from usuarios.models import Usuario, Perfil, Habilidade
from usuarios.serializers import UsuarioSerializer, PerfilSerializer, HabilidadeSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioViewSet(viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de usuarios.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Usuario.objects.all().order_by('id')
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['nome', 'data_cadastro']
  filterset_fields = ['nome', 'tipo_usuario', 'email']
  serializer_class=UsuarioSerializer

class PerfilViewSet(viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de perfis.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Perfil.objects.all().order_by('id')
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['usuario__nome', 'usuario__data_cadastro', 'nivel_experiencia']
  filterset_fields = ['nivel_experiencia', 'usuario__nome', 'usuario__email']
  serializer_class=PerfilSerializer

class HabilidadeViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de habilidades.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Habilidade.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['perfis']
    serializer_class = HabilidadeSerializer