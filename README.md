# 🛰️ TOCAIA DF - Plataforma de IA Preditiva para Segurança Pública

**TOCAIA DF** é uma solução desenvolvida com o objetivo de detectar, prever e mitigar desordens urbanas com foco em **segurança pública** no Distrito Federal. Utilizamos Inteligência Artificial Generativa e Preditiva para analisar dados de redes sociais e interações com cidadãos, auxiliando o poder público na antecipação de incidentes como vandalismo e roubo.

---

## 📦 Estrutura do Projeto

```bash
📁 tocaia-df/
├── scraper/                      # Coleta e processamento de dados sociais
│   ├── twitter_scraper.py          # Código de extração de posts do X anonimizados
│   ├── requirements.txt        # Pacotes utilizados
│   └── incidentes_detectados.json  # Saída estruturada com as desordens urbanas identificadas
├── chatbot/                      # Chatbot configurado no Botpress
│   └── README.md      # Link e Prompt com as instruções para o comportamento do assistente

├── README.md                     # Este arquivo
