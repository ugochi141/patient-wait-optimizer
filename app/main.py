from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="patient-wait-optimizer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"project": "patient-wait-optimizer", "status": "operational"}

@app.get("/health")
def health():
    return {"status": "healthy"}
