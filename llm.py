from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.gentenv("GEMINI_API_KEY")

client = genai.Client(api_key="API_KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Faça um mapeamento de risco de vandalismo em Brasília, DF.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)