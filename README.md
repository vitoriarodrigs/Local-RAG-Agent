<div align="center">

🤖 **Local-RAG-Agent**  
🔐 _Seu Copilot Privativo (100% Offline)_

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20UI-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-Orchestration-4B8BBE" />
  <img src="https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/FAISS-Vector%20DB-0099E5" />
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-000000?logo=ollama&logoColor=white" />
</p>

### 📌 Sobre o Projeto

Este projeto implementa um agente de IA local em Python capaz de responder perguntas com base em documentos **PDF armazenados na máquina**, utilizando arquitetura **RAG (Retrieval-Augmented Generation)**.

Tudo é executado **100% offline**, garantindo **privacidade total**, já que nenhum dado é enviado para servidores externos.
A interface foi construída com **Streamlit** para oferecer uma experiência de chat fluida e amigável.

---

## 🛠️ Tecnologias Utilizadas

| Categoria      | Tecnologias                      |
| -------------- | -------------------------------- |
| Linguagem      | Python 3.12                      |
| Interface Web  | Streamlit                        |
| Orquestração   | LangChain                        |
| IA Local       | Llama 3 / Phi-3 via Ollama       |
| Embeddings     | `all-MiniLM-L6-v2` (HuggingFace) |
| Banco Vetorial | FAISS                            |

---

## 🚀 Funcionalidades

* [x] **Upload de PDF** via interface
* [x] **Chunking inteligente** dos documentos com sobreposição
* [x] **Busca semântica** usando embeddings
* [x] **Respostas via LLM local**
* [x] **Execução offline** e **privativa**
* [ ] Suporte a múltiplos arquivos simultâneos
* [ ] Memória de curto prazo no chat

---

## 💻 Como Instalar e Rodar

> Pré-requisitos: Python 3.12 e [Ollama](https://ollama.com/) instalados

### 1️⃣ Criar Ambiente Virtual

```bash
python -m venv venv
```

### 2️⃣ Ativar Ambiente

**Windows**

```bash
venv\Scripts\activate
```

**Linux / MacOS**

```bash
source venv/bin/activate
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Baixar o Modelo no Ollama

Certifique-se de que o Ollama está rodando e execute:

```bash
ollama pull phi3
```

### 5️⃣ Iniciar a Aplicação

```bash
streamlit run app.py
```

---

## 🏗️ Estrutura de Pastas

```bash
.
├── app.py               # Interface web e lógica principal
├── agente_pro.py        # Versão para terminal (backend original)
├── requirements.txt     # Dependências do projeto
└── .gitignore           # Arquivos ignorados pelo Git
```

---

## 🧱 Arquitetura RAG (Resumo)

> Fluxo simplificado do pipeline:

1. Upload do PDF → extração do texto
2. Chunking com sobreposição
3. Embeddings via HuggingFace
4. Armazenamento vetorial no FAISS
5. Busca semântica
6. Geração final via Phi-3/Llama local

---

## 🚧 Status do Projeto ( Concluído)

Atualmente o projeto está implementado com:

✔ Motor de busca vetorial
✔ Integração com LLM local
✔ Interface gráfica em Streamlit
✔ Suporte multi-PDF
✔ Memória de contexto no chat
---

## 👩‍💻 Autora

**Desenvolvido por:** *Vitoria*

---
