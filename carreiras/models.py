from django.db import models
from usuarios.models import Usuario

class Atividade(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.CharField(max_length=300)
  categoria = models.CharField(max_length=100)
  duracao_minutos = models.IntegerField()
  prioridade = models.IntegerField(choices= [
    (1, "Alta"),
    (2, "Média"),
    (3, "Baixa"),
  ], default=3)

  recomendacao = models.ForeignKey(
        "Recomendacao",
        on_delete=models.CASCADE,
        related_name="atividades",
        null=True,
        blank=True
  )

  def __str__(self):
    return f"{self.titulo} - {self.categoria}"


class Recomendacao(models.Model):
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

  tema = models.CharField(max_length=200)
  subtema = models.CharField(max_length=200, blank=True, null=True)

  descricao = models.TextField()
  recursos = models.JSONField(blank=True, null=True) #Lista de links/recursos
  status = models.CharField(
    max_length=20,
    choices=[
      ('pendente', 'Pendente'),
      ('aceita', 'Aceita'),
      ('ignorada', 'Ignorada')
    ],
    default = 'pendente'
  ) 

  #Dados IA
  payload_ia = models.JSONField(blank=True, null=True)
  explicacao_ia = models.TextField(blank=True, null=True)
  score_relevancia = models.FloatField(default=0)

  data_gerada = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.tema} - {self.subtema or ''} ({self.usuario})"


class Progresso(models.Model):
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, null=True)
  data_concluida = models.DateTimeField(blank=True, null=True)
  status = models.CharField(
    max_length=20,
    choices=[
      ('pendente', 'Pendente'),
      ('em_andamento', 'Em andamento'),
      ('concluida', 'Concluída')
    ],
    default = 'pendente'
  )

  def __str__(self):
    return f"{self.usuario} - {self.atividade} : {self.status}"