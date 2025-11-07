from usuarios.models import Usuario, Perfil, Habilidade
from usuarios.serializers import UsuarioSerializer, PerfilSerializer, HabilidadeSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de usuarios.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Usuario.objects.all().order_by('id')
  serializer_class=UsuarioSerializer

class PerfilViewSet(viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de perfis.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Perfil.objects.all().order_by('id')
  serializer_class=PerfilSerializer

class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer