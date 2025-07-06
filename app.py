from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langdetect import detect
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
llm = ChatOpenAI(temperature=0.3, model_name="gpt-4")
qa_chain = ConversationalRetrievalChain.from_llm(llm, vectordb.as_retriever())

PERSONALITY_PROMPT = """
You are DesiGPT, a warm and respectful AI knowledgeable in Indian history, culture, languages.
"""

class Query(BaseModel):
    question: str
    chat_history: list = []

@app.post("/ask")
async def ask_question(query: Query):
    lang = detect(query.question)
    if lang == "hi":
        personality = PERSONALITY_PROMPT + "\nPlease answer in Hindi."
    elif lang == "sa":
        personality = PERSONALITY_PROMPT + "\nPlease answer in Sanskrit."
    else:
        personality = PERSONALITY_PROMPT + "\nPlease answer in English."

    response = qa_chain({
        "question": personality + "\n\n" + query.question,
        "chat_history": query.chat_history
    })
    return {"answer": response["answer"]}
