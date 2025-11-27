"""
FastAPI application for SpeakWise Real pitch coaching service.
"""
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from .models import PitchAnalysisRequest, PitchAnalysisResponse, TranscriptionResponse
from .coach import SpeakWiseCoach
from .transcription import TranscriptionService

# Load environment variables
load_dotenv()

app = FastAPI(
    title="SpeakWise Real API",
    description="AI-powered pitch and communication coaching API",
    version="1.0.0"
)

# Configure CORS
# Get allowed origins from environment or use defaults
allowed_origins = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:5173"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
coach = SpeakWiseCoach()
transcription_service = TranscriptionService()


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


@app.post("/api/transcribe-audio", response_model=TranscriptionResponse)
async def transcribe_audio(
    file: UploadFile = File(..., description="Audio file to transcribe"),
    model_id: str = Form(default="scribe_v1", description="Model to use for transcription"),
    language_code: str = Form(default="eng", description="Language code (e.g., 'eng', 'pt', 'es')"),
    diarize: bool = Form(default=True, description="Whether to annotate who is speaking"),
    tag_audio_events: bool = Form(default=True, description="Tag audio events like laughter, applause")
):
    """
    Transcribe an audio file to text using ElevenLabs.
    
    Supported audio formats: MP3, WAV, M4A, FLAC, etc.
    
    Returns the transcribed text that can be used with the analyze-pitch endpoint.
    """
    try:
        # Read audio file
        audio_bytes = await file.read()
        
        # Validate file size (optional: limit to 25MB)
        max_size = 25 * 1024 * 1024  # 25MB
        if len(audio_bytes) > max_size:
            raise HTTPException(
                status_code=413,
                detail=f"File too large. Maximum size is {max_size / 1024 / 1024}MB"
            )
        
        # Transcribe
        transcript = transcription_service.transcribe_audio(
            audio_file=audio_bytes,
            model_id=model_id,
            language_code=language_code if language_code else None,
            diarize=diarize,
            tag_audio_events=tag_audio_events
        )
        
        return TranscriptionResponse(
            transcript=transcript,
            model_used=model_id,
            language=language_code
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid request: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error transcribing audio: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

