from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up patient-wait-optimizer...")
    yield
    logger.info("Shutting down patient-wait-optimizer...")

app = FastAPI(
    title="patient-wait-optimizer",
    description="AI-powered queue management system for phlebotomy services with predictive wait times",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "project": "patient-wait-optimizer",
        "status": "operational",
        "description": "AI-powered queue management system for phlebotomy services with predictive wait times"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/status")
async def api_status():
    return {
        "api_version": "v1",
        "status": "operational",
        "endpoints_available": True
    }
