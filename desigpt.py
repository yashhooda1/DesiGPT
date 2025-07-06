from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langdetect import detect
from dotenv import load_dotenv
import os

load_dotenv()

# Load embedding & vector DB
embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="db", embedding_function=embeddings)

# Build QA chain with retrieval
llm = ChatOpenAI(temperature=0.3, model_name="gpt-4")
qa_chain = ConversationalRetrievalChain.from_llm(llm, vectordb.as_retriever())

# Warm respectful personality template
PERSONALITY_PROMPT = """
You are DesiGPT, an AI expert on Indian culture, history, spirituality, and languages.
Speak warmly, with cultural respect, using Hindi or Sanskrit if the user prefers.
"""

def handle_query(user_query, chat_history=[]):
    lang = detect(user_query)
    if lang == "hi":
        personality = PERSONALITY_PROMPT + "\nRespond in Hindi."
    elif lang == "sa":
        personality = PERSONALITY_PROMPT + "\nRespond in Sanskrit."
    else:
        personality = PERSONALITY_PROMPT + "\nRespond in English."

    # Inject personality into context
    response = qa_chain({
        "question": personality + "\n\n" + user_query,
        "chat_history": chat_history
    })
    return response["answer"]

if __name__ == "__main__":
    history = []
    while True:
        user_input = input("Ask DesiGPT: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = handle_query(user_input, history)
        print("\nDesiGPT:", answer)
        history.append((user_input, answer))
