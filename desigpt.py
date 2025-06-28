import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

load_dotenv()

# Step 1: Load and split Hindi PDFs
loader = PyPDFLoader("data/bhagavad_gita_hindi.pdf")
pages = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(pages)

# Step 2: Create embeddings
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

# Step 3: Build Retrieval-based QA
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)

# Step 4: Ask a question
#query = "भगवद गीता में अर्जुन को क्या सिखाया गया?"
#response = qa_chain.run(query)
#print(response)
