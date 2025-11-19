from carreiras.models import Atividade, Recomendacao, Progresso
from usuarios.models import Perfil, Usuario
from carreiras.serializers import AtividadeSerializer, RecomendacaoSerializer, ProgressoSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from carreiras.services.ia_perplexity import Recomender
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
  filterset_fields = ['usuario__nome', 'usuario__user__email', 'status']
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
    filterset_fields = ['usuario__nome', 'usuario__user__email', 'status', 'data_concluida']
    serializer_class = ProgressoSerializer

class GerarRoadMapView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_django = request.user
        try:
            usuario = user_django.usuario
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não possui perfil extendido (Usuario)"}, status=400)

        objetivo = request.data.get("objetivo")
        if not objetivo:
            return Response({"erro": "O campo 'objetivo' é obrigatório"}, status=400)

        if "tema" not in objetivo:
            return Response({"erro": "O campo objetivo.tema é obrigatório"}, status=400)

        perfil = Perfil.objects.filter(usuario=usuario).first()
        if not perfil:
            return Response({"erro": "Perfil não encontrado para o usuário autenticado"}, status=404)

        payload = Recomender.gerar_roadmap(perfil, objetivo)

        recomendacao = Recomendacao.objects.create(
            usuario=usuario,
            tema=payload["tema"],
            subtema=payload["subtema"],
            descricao=payload["descricao"],
            recursos=payload["recursos"],
            payload_ia=payload
        )

        atividades_criadas = []
        for act in payload.get("atividades", []):
            atividade = Atividade.objects.create(
                titulo=act["titulo"],
                descricao=act["descricao"],
                categoria=act["categoria"],
                duracao_minutos=act["duracao_minutos"],
                prioridade=act["prioridade"]
            )
            atividades_criadas.append(atividade)

            Progresso.objects.create(
                usuario=usuario,
                atividade=atividade,
                status="pendente"
            )

        return Response({
            "recomendacao_id": recomendacao.id,
            "atividades": [a.id for a in atividades_criadas]
        })
