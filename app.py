import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="AI Local Multi-Doc", page_icon="📚", layout="centered")

# Estilo Dark customizado
st.markdown("""
    <style>
    .stApp { max-width: 800px; margin: 0 auto; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def carregar_ia():
    # Usando phi3:mini para ser mais rápido na resposta
    return OllamaLLM(model="phi3:mini", timeout=120)

llm = carregar_ia()
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# --- INICIALIZAÇÃO DA MEMÓRIA ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar para múltiplos arquivos
with st.sidebar:
    st.title("📂 Gestão de Documentos")
    uploaded_files = st.file_uploader("Suba seus PDFs", type="pdf", accept_multiple_files=True)
    
    if st.button("Limpar Histórico"):
        st.session_state.messages = []
        st.rerun()

st.title("💬 Multi-Doc Chat")
st.caption("Converse com vários documentos ao mesmo tempo localmente.")

# --- PROCESSAMENTO DE MÚLTIPLOS ARQUIVOS ---
if uploaded_files:
    all_chunks = []
    
    with st.status("Processando documentos...", expanded=False) as status:
        for uploaded_file in uploaded_files:
            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            loader = PyPDFLoader(temp_path)
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            chunks = text_splitter.split_documents(docs)
            all_chunks.extend(chunks)
            os.remove(temp_path) # Limpa o arquivo temporário
            st.write(f"✅ {uploaded_file.name} processado.")
        
        # Cria a base vetorial única com todos os arquivos
        vector_db = FAISS.from_documents(all_chunks, embeddings)
        status.update(label="Documentos Indexados!", state="complete")

    # Exibe histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt_usuario := st.chat_input("Pergunte algo sobre os arquivos..."):
        st.session_state.messages.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)

        with st.chat_message("assistant"):
            with st.spinner("Analisando documentos..."):
                # Busca contexto nos múltiplos arquivos
                contexto_relevante = vector_db.similarity_search(prompt_usuario, k=3)
                contexto_texto = "\n".join([doc.page_content for doc in contexto_relevante])
                
                # --- LÓGICA DE MEMÓRIA DE CURTO PRAZO ---
                historico_recente = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-3:-1]])
                
                prompt_final = f"""Você é um assistente prestativo. Use o histórico e o contexto para responder.
                
                HISTÓRICO RECENTE:
                {historico_recente}
                
                CONTEXTO DOS DOCUMENTOS:
                {contexto_texto}
                
                PERGUNTA: {prompt_usuario}"""
                
                resposta = llm.invoke(prompt_final)
                st.markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})
else:
    st.info("Suba um ou mais PDFs na barra lateral para começar a análise.")
