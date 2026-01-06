import sys
import io
from langchain_ollama import OllamaLLM

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configura o modelo
model = OllamaLLM(model="llama3")

print("--- 🤖 Agente Iniciado ---")

# Faz uma pergunta via Python
pergunta = "Explique brevemente o que é um agente RAG para um iniciante."
resposta = model.invoke(pergunta)

print(f"Pergunta: {pergunta}")
print("-" * 30)
print(f"Resposta da IA: {resposta}")