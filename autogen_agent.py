from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv

load_dotenv()

# Embed + retriever
embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
retriever = vectordb.as_retriever()

# Tools for agent
search = DuckDuckGoSearchRun()
tools = [
    Tool(name="Search", func=search.run, description="Useful for current events"),
    Tool(name="Vector Retriever", func=lambda q: retriever.get_relevant_documents(q), description="Fetch historical data from DB")
]

# Build agent
llm = ChatOpenAI(temperature=0.3, model_name="gpt-4")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Autonomous loop
while True:
    user_input = input("DesiGPT Agent: Ask anything > ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = agent.run(user_input)
    print("\nDesiGPT Agent:", result)
