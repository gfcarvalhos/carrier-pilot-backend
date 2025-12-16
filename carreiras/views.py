from carreiras.models import Atividade, Recomendacao, Progresso
from carreiras.serializers import AtividadeSerializer, RecomendacaoSerializer, ProgressoSerializer, GerarRoadmapInputSerializer
from usuarios.models import Perfil
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from carreiras.services.generate_recomendation import gerar_roadmap_para_perfil
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.mixin.mixins import UniversalUserFilterMixin, IndirectUserFilterMixin
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

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

class RecomendacaoViewSet(UniversalUserFilterMixin, viewsets.ModelViewSet):
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de Recomendacao.

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE
  """
  queryset= Recomendacao.objects.all().order_by('id')
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['usuario__nome', 'usuario__data_cadastro', 'status', 'data_gerada']
  filterset_fields = ['usuario__nome', 'usuario__user__email', 'status']
  serializer_class=RecomendacaoSerializer

  @action(detail=False, methods=["get"], url_path="por-perfil/(?P<perfil_id>[^/.]+)")
  def por_perfil(self, request, perfil_id=None):
      """
      GET /recomendacoes/por-perfil/<perfil_id>/
      Retorna recomendações filtradas pelo id do perfil.
      """
      qs = self.get_queryset().filter(perfil_id=perfil_id)
      serializer = self.get_serializer(qs, many=True)
      return Response(serializer.data)

class ProgressoViewSet(UniversalUserFilterMixin, viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de Progresso.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Progresso.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario__nome', 'usuario__data_cadastro', 'data_concluida', 'status']
    filterset_fields = ['usuario__nome', 'usuario__user__email', 'status', 'data_concluida']
    serializer_class = ProgressoSerializer


class AtividadeViewSet(IndirectUserFilterMixin, viewsets.ModelViewSet):
    user_relation = "recomendacao__usuario"
    queryset = Atividade.objects.all().order_by('id')
    serializer_class = AtividadeSerializer
    http_method_names = ["get", "put"]

class GerarRoadMapView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GerarRoadmapInputSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = request.user.usuario
        perfil_id = serializer.validated_data["perfil_id"]

        perfil = get_object_or_404(Perfil, id=perfil_id, usuario=usuario)
        recomendacao, atividades = gerar_roadmap_para_perfil(perfil)

        return Response({
            "recomendacao_id": recomendacao.id,
            "atividades": [a.id for a in atividades],
        })
