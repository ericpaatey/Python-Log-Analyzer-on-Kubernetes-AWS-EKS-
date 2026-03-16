from fastapi import FastAPI, UploadFile
from analyzer import analyze_logs
from db import insert_result

app = FastAPI(title="Kubernetes Log Analyzer")

@app.get("/")
def home():
    return {"message": "Log Analyzer API running on Kubernetes"}

@app.post("/analyze")
async def analyze(file: UploadFile):

    contents = await file.read()
    logs = contents.decode().splitlines()

    result = analyze_logs(logs)

    insert_result(result)

    return result