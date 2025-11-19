from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
  TIPO_USUARIO_CHOICES = (
    ('G', 'gratuito'),
    ('P', 'premium')
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')

  nome = models.CharField(max_length=100)
  data_cadastro = models.DateTimeField(auto_now_add=True)
  tipo_usuario = models.CharField(max_length=1, blank=False, null=False, choices=TIPO_USUARIO_CHOICES, default = 'G')

  def __str__(self):
        return f"{self.nome} ({self.tipo_usuario})"

class Perfil (models.Model):
  NIVEL_EXPERIENCIA_CHOICES = (
     ('J', 'junior'),
     ('P', 'pleno'),
     ('S', 'senior')
  )
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='perfis')
  area_interesse = models.CharField(max_length=100)
  nivel_experiencia = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL_EXPERIENCIA_CHOICES, default = 'J')
  objetivo_pessoal = models.TextField(blank=True, null=True)
  criado_em = models.DateTimeField(default=timezone.now)

  def __str__(self):
        return f"{self.usuario} ({self.usuario.email})"

class Habilidade (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    perfis = models.ManyToManyField(Perfil, related_name='habilidades',blank=True)

    def __str__(self):
      return f"{self.nome}"