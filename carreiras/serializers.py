from rest_framework import serializers
from carreiras.models import Atividade, Recomendacao, Progresso

class AtividadeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Atividade
    fields = '__all__'

class RecomendacaoSerializer(serializers.ModelSerializer):
  usuario_nome = serializers.CharField(source="usuario.nome", read_only=True)
  usuario_email = serializers.CharField(source="usuario.user.email", read_only=True)
  class Meta:
    model = Recomendacao
    fields = '__all__'

class ProgressoSerializer(serializers.ModelSerializer):
  usuario_nome = serializers.CharField(source="usuario.nome", read_only=True)
  usuario_email = serializers.CharField(source="usuario.user.email", read_only=True)
  class Meta:
      model = Progresso
      fields = '__all__'

class GerarRoadmapInputSerializer(serializers.Serializer):
    perfil_id = serializers.IntegerField()