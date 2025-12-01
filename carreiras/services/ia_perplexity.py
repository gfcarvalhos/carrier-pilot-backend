import os
from perplexity import Perplexity
import json

client = Perplexity(api_key=os.getenv("PERPLEXITY_API_KEY"))

class Recomender:
  @staticmethod
  def gerar_roadmap(perfil):
    prompt = Recomender._montar_prompt(perfil)

    response = client.chat.completions.create(
            model="sonar",
            messages=[{"role": "user", "content": prompt}],
            stream=False
    )
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
      return json.loads(resposta_texto)
    except:
      raise ValueError("A IA não retornou um JSON válido")
