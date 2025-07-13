# main.py — FastAPI + Streamlit hybrid server for Cloud Run

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import subprocess
import threading

app = FastAPI()

# Background thread to launch Streamlit UI on port 8080
def run_streamlit():
    subprocess.run([
        "streamlit", "run", "growth_dashboard.py",
        "--server.port=8080",  # 👈 MUST match Cloud Run
        "--server.address=0.0.0.0"
    ])

@app.on_event("startup")
def startup_event():
    threading.Thread(target=run_streamlit, daemon=True).start()

@app.get("/")
async def root():
    return RedirectResponse(url="/")

@app.get("/dashboard")
async def dashboard():
    return {"message": "Etsy Commander dashboard active at /"}

@app.get("/status")
async def status():
    return {"status": "Commander is live", "agents_online": 5, "listings_created": 12}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
