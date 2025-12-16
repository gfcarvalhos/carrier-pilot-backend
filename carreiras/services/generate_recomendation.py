from carreiras.models import Recomendacao, Atividade, Progresso
from usuarios.models import Perfil
from carreiras.services.ia_perplexity import Recomender

def gerar_roadmap_para_perfil(perfil: Perfil) -> Recomendacao:  
  payload = Recomender.gerar_roadmap(perfil)

  if not isinstance(payload, dict):
        raise ValueError(f"Payload inválido da IA: {type(payload)} - {payload}")
  
  recomendacao = Recomendacao.objects.create(
        usuario=perfil.usuario,
        tema=payload.get("tema", ""),
        subtema=payload.get("subtema", ""),
        descricao=payload.get("descricao", ""),
        recursos=payload.get("recursos", []),
        payload_ia=payload,
    )

  atividades_criadas = []
  for act in payload.get("atividades", []):
      
      if not isinstance(act, dict):
            continue
      
      atividade = Atividade.objects.create(
          titulo=act.get("titulo", ""),
          descricao=act.get("descricao", ""),
          categoria=act.get("categoria", ""),
          duracao_minutos=act.get("duracao_minutos", 0),
          prioridade=act.get("prioridade", 1),
      )
      atividades_criadas.append(atividade)

      Progresso.objects.create(
                usuario=perfil.usuario,
                atividade=atividade,
                status="pendente",
            )
  return recomendacao, atividades_criadas