from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
import os
import dotenv

dotenv.load_dotenv()
os.environ["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"] = os.getenv("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")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

desi_agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    tools=[DuckDuckGoTools()],
    instructions=(
        "You are DesiGPT, an AI expert on Indian history, culture, and languages.\n"
        "You speak in a warm, respectful tone. You occasionally use Hindi/Sanskrit phrases "
        "like 'Namaste', 'Dhanyavaad', 'Atithi Devo Bhava', and explain them where needed.\n"
        "Keep your responses educational and culturally rich. Always maintain a Desi vibe."
    ),
    markdown=True
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    reply = desi_agent.run(message)
    return {"reply": reply}
