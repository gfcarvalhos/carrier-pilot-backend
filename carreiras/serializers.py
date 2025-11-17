from rest_framework import serializers
from carreiras.models import Atividade, Recomendacao, Progresso

class AtividadeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Atividade
    fields = '__all__'

class RecomendacaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recomendacao
    fields = '__all__'

class ProgressoSerializer(serializers.ModelSerializer):
  class Meta:
      model = Progresso
      fields = '__all__'