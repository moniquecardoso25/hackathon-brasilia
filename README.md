# 🛰️ TOCAIA DF - Plataforma de IA Preditiva para Segurança Pública

**TOCAIA DF** é uma solução desenvolvida com o objetivo de detectar, prever e mitigar desordens urbanas com foco em **segurança pública** no Distrito Federal. Utilizamos Inteligência Artificial Generativa e Preditiva para analisar dados de redes sociais e interações com cidadãos, auxiliando o poder público na antecipação de incidentes como vandalismo e roubo.

---

## 📦 Estrutura do Projeto

```bash
📁 tocaia-df/
├── scraper/                      # Coleta e processamento de dados sociais
│   ├── main_scraper.py           # Código de extração de posts do X (Twitter)
│   ├── anonimiza_texto.py        # Remoção de dados pessoais
│   └── incidentes_detectados.json  # Saída estruturada com denúncias identificadas
├── chatbot/                      # Chatbot configurado no Botoress
│   └── prompt_instrucoes.md      # Instruções para o comportamento do assistente
├── data/                         # Dados simulados ou reais para análise
│   └── denuncias_chatbot.csv
├── README.md                     # Este arquivo
