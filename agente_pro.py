from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

# 1. Carregar o PDF
loader = PyPDFLoader("Livro de Receitas.pdf")
docs = loader.load()

# 2. Quebrar em pedaços (Chunking)
# Isso evita que a IA se perca em textos longos
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)

# 3. Criar a "Memória" (Embeddings + Vector Store)
# Esse modelo 'all-MiniLM-L6-v2' roda local e é super leve
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = FAISS.from_documents(chunks, embeddings)

# 4. Configurar a IA
llm = OllamaLLM(model="llama3")

# 5. Função de pergunta
def perguntar_ao_documento(pergunta):
    # Busca apenas os trechos relevantes no PDF
    contexto_relevante = vector_db.similarity_search(pergunta, k=3)
    contexto_texto = "\n".join([doc.page_content for doc in contexto_relevante])
    
    prompt = f"Use o contexto abaixo para responder à pergunta.\nContexto: {contexto_texto}\nPergunta: {pergunta}"
    return llm.invoke(prompt)

print("--- 🧠 Agente com Memória Ativo! ---")
pergunta_usuario = "Qual o tema principal desse documento?"
print(f"Resposta: {perguntar_ao_documento(pergunta_usuario)}")