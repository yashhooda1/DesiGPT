from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load texts
loader = TextLoader("samhaji_prompts.txt")
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Store vectors
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(docs, embeddings, persist_directory="db")
vectordb.persist()
print("Vector DB created!")
