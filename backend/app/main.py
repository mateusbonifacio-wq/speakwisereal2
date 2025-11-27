"""
FastAPI application for SpeakWise Real pitch coaching service.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from .models import PitchAnalysisRequest, PitchAnalysisResponse
from .coach import SpeakWiseCoach

# Load environment variables
load_dotenv()

app = FastAPI(
    title="SpeakWise Real API",
    description="AI-powered pitch and communication coaching API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize coach
coach = SpeakWiseCoach()


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "service": "SpeakWise Real",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/api/analyze-pitch", response_model=PitchAnalysisResponse)
async def analyze_pitch(request: PitchAnalysisRequest):
    """
    Analyze a pitch and return comprehensive structured feedback.
    
    This endpoint receives a pitch transcript and optional context,
    then returns detailed feedback following the SpeakWise Real format.
    """
    try:
        response = coach.analyze_pitch(request)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing pitch: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

