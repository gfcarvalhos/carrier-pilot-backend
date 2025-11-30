from rest_framework.exceptions import ValidationError
from usuarios.models import Usuario, Perfil, Habilidade
from usuarios.serializers import UsuarioSerializer, PerfilSerializer, HabilidadeSerializer
from usuarios.filters import PerfilFilter
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from core.mixin.mixins import RestrictToSelfMixin, OwnUserDataMixin

class UsuarioViewSet(RestrictToSelfMixin, viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de usuarios.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Usuario.objects.all().order_by('id')
  serializer_class=UsuarioSerializer

  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  filterset_fields = ['nome', 'tipo_usuario', 'user__email']
  ordering_fields = ['nome', 'data_cadastro',]
  ordering = ['id']

  def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return [IsAuthenticated()]

class PerfilViewSet(OwnUserDataMixin, viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de perfis.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Perfil.objects.all().order_by('id')
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['usuario__nome', 'usuario__data_cadastro', 'nivel_experiencia']
  filterset_class = PerfilFilter
  serializer_class=PerfilSerializer
  permission_classes = [IsAuthenticated]
  
  def perform_create(self, serializer):
      try:
        usuario = self.request.user.usuario
      except Usuario.DoesNotExist:
        raise ValidationError({"detail": "Usuário de perfil não encontrado."})
      serializer.save(usuario=usuario)

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return qs

        try:
            usuario = user.usuario
        except:
            return qs.none()

        return qs.filter(perfis__usuario=usuario).distinct()
