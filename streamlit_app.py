import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langdetect import detect
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
llm = ChatOpenAI(temperature=0.3, model_name="gpt-4")
qa_chain = ConversationalRetrievalChain.from_llm(llm, vectordb.as_retriever())

PERSONALITY_PROMPT = "You are DesiGPT, a warm, respectful expert on Indian culture and history."

st.title("🇮🇳 DesiGPT - Indian AI Chatbot")
query = st.text_input("Ask about Indian culture, history or spirituality:")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Ask"):
    lang = detect(query)
    if lang == "hi":
        personality = PERSONALITY_PROMPT + " Answer in Hindi."
    elif lang == "sa":
        personality = PERSONALITY_PROMPT + " Answer in Sanskrit."
    else:
        personality = PERSONALITY_PROMPT + " Answer in English."

    response = qa_chain({
        "question": personality + "\n\n" + query,
        "chat_history": st.session_state.chat_history
    })
    st.session_state.chat_history.append((query, response["answer"]))
    for q, a in reversed(st.session_state.chat_history):
        st.write(f"**You:** {q}")
        st.write(f"**DesiGPT:** {a}")
