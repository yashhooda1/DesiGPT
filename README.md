# 🇮🇳 DesiGPT – AI Chatbot on Indian Culture & History

DesiGPT is an AI-powered chatbot that embodies the soul of Bharat. It answers questions about Indian history, languages, festivals, and culture with warmth and respect. Built with FastAPI, Agno AGI, and OpenAI GPT-4.

## ✨ Features
- Understands Indian traditions, festivals, culture, languages
- Speaks with Desi tone (Hindi/Sanskrit phrases included)
- Powered by Agno + GPT-4 + DuckDuckGo Tools
- React frontend chat interface
- Easy to deploy and extend

## 📦 Tech Stack
- **Backend**: Python, FastAPI, Agno, OpenAI, DuckDuckGo API
- **Frontend**: React + Tailwind CSS
- **Deployment**: Vercel (frontend), Render or HuggingFace Spaces (backend)

## 🚀 Quickstart
### 1. Clone the repo
```bash
git clone https://github.com/yourusername/desigpt.git
cd desigpt
```

### 2. Setup the backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI API Key
uvicorn main:app --reload
```

### 3. Run the frontend
```bash
cd frontend
npm install
npm run dev
```
