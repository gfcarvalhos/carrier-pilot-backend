from carreiras.models import Recomendacao, Atividade, Progresso
from usuarios.models import Perfil
from carreiras.services.ia_perplexity import Recomender

def gerar_roadmap_para_perfil(perfil: Perfil) -> Recomendacao:  
  payload = Recomender.gerar_roadmap(perfil)
  
  recomendacao = Recomendacao.objects.create(
        usuario=perfil.usuario,
        perfil=perfil, 
        tema=payload["tema"],
        subtema=payload["subtema"],
        descricao=payload["descricao"],
        recursos=payload["recursos"],
        payload_ia=payload,
  )

  atividades_criadas = []
  for act in payload.get("atividades", []):
      atividade = Atividade.objects.create(
          titulo=act["titulo"],
          descricao=act["descricao"],
          categoria=act["categoria"],
          duracao_minutos=act["duracao_minutos"],
          prioridade=act["prioridade"],
      )
      atividades_criadas.append(atividade)

      Progresso.objects.create(
                usuario=perfil.usuario,
                atividade=atividade,
                status="pendente",
            )
  return recomendacao, atividades_criadas