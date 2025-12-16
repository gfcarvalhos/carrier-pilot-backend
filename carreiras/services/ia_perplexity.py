import os
from perplexity import Perplexity
import json

client = Perplexity(api_key=os.getenv("PERPLEXITY_API_KEY"))

class Recomender:
  @staticmethod
  def gerar_roadmap(perfil):
    prompt = Recomender._montar_prompt(perfil)
    try :
      response = client.chat.completions.create(
              model="sonar",
              messages=[{"role": "user", "content": prompt}],
              stream=False
      )
    except Exception as e:
      print("Erro ao chamar AI:", e)
      return None
    
    conteudo = response.choices[0].message.content
    return Recomender._parse_response(conteudo)
  
  @staticmethod
  def _montar_prompt(perfil):
    return f"""
Você é uma IA especialista em criação de roadmaps profissionais.
Gere um ROADMAP detalhado para um usuário com o seguinte perfil:
Nome: {perfil.usuario.nome}
Área de interesse: {perfil.area_interesse}
Nível de experiencia: {perfil.nivel_experiencia}
Objetivo pessoal: {perfil.objetivo_pessoal}

Responda APENAS com um JSON válido.
Não adicione explicações, markdown ou texto fora do JSON.
Formato exato esperado:
o roadmap deve seguir EXATAMENTE o formato JSON abaixo:
{{
  "tema": "...",
  "subtema": "...",
  "descricao": "...",
  "recursos": [
    {{
      "titulo": "...",
      "tipo": "youtube|artigo|curso|livro",
      "url": "..."
    }}
  ],
  "atividades": [
    {{
      "titulo": "...",
      "descricao": "...",
      "categoria": "...",
      "duracao_minutos": 120,
      "prioridade": 1
    }}
  ]
}}

RESPONDA APENAS O JSON.
"""
  @staticmethod
  def _parse_response(resposta_texto):
    try:
        data = json.loads(resposta_texto)
    except Exception:
        raise ValueError("A IA não retornou um JSON válido")

    if isinstance(data, list):
        if not data:
            raise ValueError("A IA retornou uma lista vazia")
        data = data[0]

    if not isinstance(data, dict):
        raise ValueError("Formato inesperado de resposta da IA")

    return data
