from rest_framework import serializers
from usuarios.models import Usuario, Perfil

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
  class Meta:
    model = Perfil
    fields = '__all__'