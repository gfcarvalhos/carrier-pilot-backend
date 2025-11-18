# Carrier Pilot — Projeto de Desenvolvimento Web

**Disciplina:** Desenvolvimento Web  
**Curso:** Engenharia da Computação — Universidade Federal do Maranhão (UFMA)  
**Autores:** Gabriel Felipe e Cleila Galiza

---

## 📌 Descrição

O **Carrier Pilot** é uma aplicação web desenvolvida como parte da disciplina de Desenvolvimento Web na UFMA.  
O sistema tem por objetivo apoiar o desenvolvimento profissional do usuário por meio de **perfis**, **habilidades**, **atividades**, **recomendações geradas por uma IA** e acompanhamento de **progresso**.

---

## 🧭 Estrutura do Projeto

Estrutura de alto nível:

```
carrier_pilot/
├── carrier_pilot/ # Configurações do Django (settings, urls, wsgi/asgi)
├── usuarios/ # App: Usuario, Perfil, Habilidade
├── carreira/ # App: Atividade, Recomendacao, Progresso
├── requirements.txt
├── docker-compose.yml
└── manage.py
```

### Apps principais

- **usuarios**

  - Modelos: `Usuario` (custom user), `Perfil` (1:N com Usuario), `Habilidade` (ManyToMany com Perfil)
  - Responsabilidades: autenticação, gestão de perfis, registro de habilidades

- **carreira**
  - Modelos: `Atividade`, `Recomendacao`, `Progresso`
  - Responsabilidades: estrutura de atividades, recomendações (geradas pela IA) e acompanhamento da execução

---

## 🛠 Tecnologias

- **Linguagem:** Python
- **Framework:** Django
- **API:** Django REST Framework
- **Banco de Dados:** MySQL
- **Extras:** Docker, docker-compose

---

## 🚀 Funcionalidades principais

- Cadastro e autenticação de usuários (modelo customizado baseado em `AbstractUser`)
- Perfis múltiplos por usuário (1:N) e associação de habilidades (ManyToMany)
- Gerenciamento de atividades com prioridade e duração estimada
- Recomendação estruturada (tema, subtema, recursos, dados da IA, score de relevância)
- Modelo de Progresso para rastrear a execução real das atividades
- Endpoints REST com filtros e ordenação (DRF + django-filter sugerido)

---

## 📁 Exemplos de modelos (resumo)

**Atividade**

- `titulo`, `descricao`, `categoria`, `duracao_minutos`, `prioridade`

**Recomendacao**

- `usuario` (FK), `atividade` (FK opcional), `tema`, `subtema`, `descricao`, `recursos` (JSON), `payload_ia` (JSON), `explicacao_ia`, `score_relevancia`, `status`, `data_gerada`

**Progresso**

- `usuario` (FK), `atividade` (FK), `status`, `data_concluida`

---

## ⚙️ Instalação e Execução (local)

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd carrier_pilot
   ```
2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Instale dependências:

```bash
pip install -r requirements.txt
```

4. Configure o settings.py (banco, AUTH_USER_MODEL, env vars etc.) e rode migrações:

```bash
python manage.py migrate
```

5. Rode o servidor de desenvolvimento:

```bash
python manage.py runserver
```
