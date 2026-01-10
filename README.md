# Local-RAG-Agent
# 🧠 Local AI Agent: O Meu "Copilot" Privativo

## 📌 Sobre o Projeto
Este projeto é um agente de Inteligência Artificial desenvolvido em Python que permite conversar com documentos locais (PDF, TXT) de forma 100% privada. Diferente do Copilot ou ChatGPT, nenhum dado sai da máquina, e não há custos de API, pois utiliza modelos open-source rodando localmente.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Orquestração:** LangChain (para criar a lógica do agente)
- **Modelo de IA:** Llama 3 (via Ollama)
- **Banco de Dados de Vetores:** FAISS ou ChromaDB
- **Interface:** Streamlit (Web UI)

## 🚀 Funcionalidades
- [x] Extração de texto de arquivos PDF.
- [x] Fragmentação inteligente de texto (Chunking) para alta performance.
- [x] Busca semântica por similaridade (o agente entende o contexto).
- [ ] Upload de documentos via interface Web.
- [ ] Chat interativo com histórico de conversa.
- [x] Execução 100% offline e gratuita.

---

## 💻 Como Instalar e Rodar

1. Configurar o Ambiente Virtual
# Criar o ambiente
python -m venv venv

# Ativar o ambiente (Windows)
source venv/Scripts/activate.

2. Instalar Dependências
Bash
pip install langchain-community langchain-ollama langchain-huggingface pypdf faiss-cpu sentence-transformers

3. Baixar Modelos no Ollama
Bash
ollama pull llama3
ollama pull phi3

4. Executar o Agente
Bash
python agente_pro.py
---
## 🚧 Status do Projeto
Em desenvolvimento 🛠️ Próximo passo: Implementação da interface gráfica com Streamlit.
Desenvolvido por Vitoria
