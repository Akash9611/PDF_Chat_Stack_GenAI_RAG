import os, tempfile
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore   # swap for FAISS if desired
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pinecone import Pinecone

INDEX_NAME = "pdf-chat"
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def init_chain():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(INDEX_NAME)
    vectorstore = PineconeVectorStore(index, embeddings)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=False
    )

def ingest_pdf(stream: io.BytesIO, filename: str):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(stream.read())
        tmp.flush()
        loader = PyPDFLoader(tmp.name)
        docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    PineconeVectorStore.from_documents(
        chunks,
        embeddings,
        index_name=INDEX_NAME,
        namespace=filename
    )