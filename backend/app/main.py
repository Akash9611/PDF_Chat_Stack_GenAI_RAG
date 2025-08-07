from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from rag import init_chain, ingest_pdf
import io, os

app = FastAPI(title="Chat-with-PDF API")
qa_chain = init_chain()          # warmed at start-up

class Ask(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(400, "Not a PDF")
    content = await file.read()
    ingest_pdf(io.BytesIO(content), file.filename)
    return {"status": "ingested"}

@app.post("/ask")
async def ask(req: Ask):
    answer = qa_chain.invoke(req.question)["result"]
    return {"answer": answer}