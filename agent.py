import os
from dotenv import load_dotenv
import google.generativeai as genai
from crewai import Agent, Task, Crew

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define o agente
monitor_agent = Agent(
    role="Especialista em Monitoramento Urbano",
    goal="Identificar riscos urbanos e propor ações preventivas",
    backstory="Você trabalha em órgão de segurança pública de Brasília, cuidando da segurança e infraestrutura urbana.",
    llm="gemini-2.5-flash"
)

# Define uma tarefa de exemplo
tarefa = Task(
    description="Analise o seguinte relato de ocorrência urbana: 'Forte chuva deixou ruas alagadas no bairro Central e interrompeu o trânsito.'",
    expected_output="Um plano com 2 ações imediatas da prefeitura e uma recomendação de longo prazo.",
    agent=monitor_agent
)

# Define a crew (missão)
equipe = Crew(
    agents=[monitor_agent],
    tasks=[tarefa],
    verbose=True
)

resultado = equipe.kickoff()
print("\n🔍 Resposta do agente:\n")
print(resultado)
