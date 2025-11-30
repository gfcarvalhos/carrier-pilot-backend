from rest_framework import serializers
from django.contrib.auth.models import User
from usuarios.models import Usuario, Perfil, Habilidade

class UsuarioSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(write_only=True)
  senha = serializers.CharField(write_only=True, required=False)
  
  class Meta:
      model = Usuario
      fields = ['id', 'nome', 'email', 'tipo_usuario', 'data_cadastro', 'senha']

  def create(self, validated_data):
      email = validated_data.pop("email")
      senha = validated_data.pop("senha", None)

      user = User.objects.create(
          username=email,
          email=email,
      )

      if senha:
          user.set_password(senha)
      else:
          user.set_unusable_password()

      user.save()

      usuario = Usuario.objects.create(
          user=user,
          **validated_data
      )

      return usuario

  def update(self, instance, validated_data):
      email = validated_data.pop("email", None)
      senha = validated_data.pop("senha", None)

      if email:
          instance.user.email = email
          instance.user.username = email
          instance.user.save()

      if senha:
          instance.user.set_password(senha)
          instance.user.save()

      instance.nome = validated_data.get("nome", instance.nome)
      instance.tipo_usuario = validated_data.get("tipo_usuario", instance.tipo_usuario)
      instance.save()

      return instance

class PerfilSerializer(serializers.ModelSerializer):
  class Meta:
    model = Perfil
    fields = '__all__'
    read_only_fields = ['usuario']

class HabilidadeSerializer(serializers.ModelSerializer):
  class Meta:
      model = Habilidade
      fields = '__all__'