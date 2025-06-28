from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from desigpt import run_desigpt_logic  # 👈 import your logic here

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DesiGPT API is live!"}

@app.post("/ask")
async def ask(request: Request):
    try:
        body = await request.json()
        question = body.get("question", "")
        if not question:
            return JSONResponse(status_code=400, content={"error": "Missing 'question'"})

        answer = run_desigpt_logic(question)
        return JSONResponse(content={"answer": answer})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Optional if running locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
