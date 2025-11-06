from django.db import models

class Usuario(models.Model):
  TIPO_USUARIO_CHOICES = (
    ('G', 'gratuito'),
    ('P', 'premium')
  )
  nome = models.CharField(max_length=100)
  email = models.EmailField(blank=False, max_length=30)
  data_cadastro = models.DateTimeField()
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
  nivel_experiencia = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL_EXPERIENCIA_CHOICES, default = 'j')
  objetivo_pessoal = models.TextField(blank=True, null=True)

  def __str__(self):
        return f"{self.usuario} ({self.nivel_experiencia})"
