import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

# Configuração da Página - Visual Dark/Moderno
st.set_page_config(page_title="AI Local Doc", page_icon="🤖", layout="centered")

# CSS para deixar o visual mais limpo
st.markdown("""
    <style>
    .stApp { max-width: 800px; margin: 0 auto; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def carregar_ia():
    return OllamaLLM(model="phi3", timeout=120)

llm = carregar_ia()
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Inicializa o histórico de chat na memória do navegador
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("📂 Configurações")
    uploaded_file = st.file_uploader("Upload do PDF", type="pdf")
    if st.button("Limpar Chat"):
        st.session_state.messages = []
        st.rerun()

# Interface Principal
st.title("💬 Chat com seu Documento")
st.caption("Privacidade total: Seus dados não saem desta máquina.")

# Processamento do PDF
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)
    vector_db = FAISS.from_documents(chunks, embeddings)

    # Exibe as mensagens do histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Campo de Chat (Input)
    if prompt_usuario := st.chat_input("Pergunte algo sobre o PDF..."):
        # Adiciona pergunta do usuário ao chat
        st.session_state.messages.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)

        # Resposta da IA
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                contexto = vector_db.similarity_search(prompt_usuario, k=3)
                contexto_texto = "\n".join([doc.page_content for doc in contexto])
                
                prompt_final = f"Contexto: {contexto_texto}\n\nPergunta: {prompt_usuario}"
                resposta = llm.invoke(prompt_final)
                st.markdown(resposta)
        
        # Salva a resposta da IA no histórico
        st.session_state.messages.append({"role": "assistant", "content": resposta})

else:
    st.info("👋 Olá! Comece fazendo o upload de um arquivo PDF na barra lateral.")