---

# 🛠️ Tocaia DF - Twitter Scraper

## 📌 Visão Geral

Este script Python utiliza a API do Twitter (X) via Tweepy para buscar, filtrar e salvar em JSON publicações recentes relacionadas a **incidentes urbanos de segurança pública** no Distrito Federal e região. Ele faz parte do MVP da plataforma **Tocaia DF**, criada durante a CPBR17.

---

## 🎯 Objetivo

Identificar tweets com relatos de **desordens urbanas** como:

* Alagamentos
* Enchentes
* Falta de luz
* Assaltos
* Lixo acumulado
* Buracos nas ruas

Com foco especial em ocorrências **localizadas no Distrito Federal (DF)** e entorno.

---

## 🧱 Estrutura do Script

### Dependências:

* Python 3.x
* Tweepy

```bash
pip install tweepy
```

---

### Credenciais:

Preencha seu **bearer token** da API do X:

```python
bearer_token = "SUA_API_KEY_AQUI"
```

---

### Parâmetros de busca:

#### Palavras-chave de incidentes:

```python
palavras_chave = ["enchente", "alagamento", "assalto", "falta de luz", "lixo", "buraco"]
```

---

#### Palavras-chave de região (contexto geográfico):

```python
filtros_regiao = ["brasília", "bsb", "asa norte", "unb", "ceilandia", "taguatinga", "gama", "samambaia", "planaltina"]
```

---

#### Termos de contexto urbano (evitar tweets fora de contexto):

```python
termos_contexto = ["rua", "avenida", "bairro", "energia", "alagamento", "enchente", "falta de luz", "trânsito", "problema", "cidade", "governo", "denúncia", "CEB", "IPES"]
```

---

### Lógica de Filtro:

Para um tweet ser considerado relevante, ele precisa obrigatoriamente ter:

✅ Pelo menos **uma palavra-chave de incidente**
✅ Pelo menos **uma região do DF**
✅ Pelo menos **um termo de contexto urbano**

---

### Exemplo da Query Montada:

```bash
(enchente OR alagamento OR assalto OR falta de luz OR lixo OR buraco) (brasília OR bsb OR "asa norte" OR unb OR ceilandia OR taguatinga OR gama OR samambaia OR planaltina) lang:pt
```

---

## 🚀 Execução:

```bash
python scraper/twitter_scraper.py
```

O script aguarda 15 segundos antes da busca para evitar **Rate Limit**.

---

## 📤 Saída:

Gera um arquivo JSON chamado:

```bash
incidentes_detectados_x.json
```

### Estrutura de cada registro exportado:

```json
{
    "texto": "Texto do tweet...",
    "incidentes_detectados": ["alagamento", "falta de luz"],
    "regioes_detectadas": ["Asa Norte", "Brasília"],
    "data": "2025-06-21",
    "tweet_id": 1234567890,
    "link": "https://twitter.com/user/status/1234567890",
    "geo": "Não disponível"
}
```

---

## ✅ Limitações da API Gratuita:

* Apenas tweets dos **últimos 7 dias**
* **Limite de requisições por janela de tempo**
* Sem acesso a dados detalhados de geolocalização (field `geo` geralmente vazio)

---

## 🏆 Próximos passos (Melhorias futuras):

* Integração com base de dados
* Treinamento de modelo LLM para classificação automática de relevância
* Integração com canal de denúncia via WhatsApp
* Dashboard de visualização em tempo real

---

## ✅ Foco nos Critérios da Hackathon:

| Critério                     | Como atendemos                               |
| ---------------------------- | -------------------------------------------- |
| Criatividade e originalidade | Uso de mineração social geolocalizada + IA   |
| Aplicabilidade               | Detecção real de problemas urbanos           |
| Qualidade do protótipo       | Exporta dados estruturados e utilizáveis     |
| Tecnologia                   | Uso de API do X + Python + NLP básico        |
| Elemento Futuro              | Base pronta para LLM + integração multicanal |

---
