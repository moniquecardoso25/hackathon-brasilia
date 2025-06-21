import tweepy
import json
from datetime import datetime
import time

bearer_token = "SUA_API_KEY_AQUI"

client = tweepy.Client(bearer_token=bearer_token)

# Palavras-chave de incidentes
palavras_chave = ["enchente", "alagamento", "assalto", "falta de luz", "lixo", "buraco"]

# Palavras de localização
filtros_regiao = ["brasília", "bsb", "asa norte", "unb", "ceilandia", "taguatinga", "gama", "samambaia", "planaltina"]

# Termos de contexto urbano (para evitar pegar tweets sobre futebol, música, etc)
termos_contexto = ["rua", "avenida", "bairro", "energia", "alagamento", "enchente", "falta de luz", "trânsito", "problema", "cidade", "governo", "denúncia", "CEB", "IPES"]

# Monta a query mais restrita
query_incidentes = " OR ".join(palavras_chave)
query_regioes = " OR ".join([f'"{r}"' if " " in r else r for r in filtros_regiao])

query = f"({query_incidentes}) ({query_regioes}) lang:pt"

print(f"Buscando tweets com query:\n{query}")

print("Aguardando 15 segundos para evitar rate limit...")
time.sleep(15)

response = client.search_recent_tweets(
    query=query,
    tweet_fields=["created_at", "geo", "text", "lang"],
    max_results=20
)

resultados = []

if response.data:
    for tweet in response.data:
        texto = tweet.text.lower()

        incidentes = [p for p in palavras_chave if p in texto]
        regioes_mencionadas = [r for r in filtros_regiao if r in texto]
        contexto_urbano = any(c in texto for c in termos_contexto)

        # Agora só salva se: tem incidente + tem região + tem contexto urbano
        if incidentes and regioes_mencionadas and contexto_urbano:
            resultado = {
                "texto": tweet.text,
                "incidentes_detectados": incidentes,
                "regioes_detectadas": regioes_mencionadas,
                "data": tweet.created_at.strftime("%Y-%m-%d"),
                "tweet_id": tweet.id,
                "link": f"https://twitter.com/user/status/{tweet.id}",
                "geo": tweet.geo if tweet.geo else "Não disponível"
            }
            resultados.append(resultado)

    with open("incidentes_detectados_x.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)

    print(f"Exportados {len(resultados)} tweets relevantes.")
else:
    print("Nenhum tweet encontrado.")
