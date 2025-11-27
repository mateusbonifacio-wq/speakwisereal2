# SpeakWise Real Backend

FastAPI backend for the SpeakWise Real pitch coaching service.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```bash
cp .env.example .env
```

4. Add your API keys to `.env`:
```
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_MODEL=gemini-pro
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

5. Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### POST `/api/transcribe-audio`

Transcribes an audio file to text using ElevenLabs.

**Request:** Multipart form data
- `file`: Audio file (MP3, WAV, M4A, FLAC, WEBM)
- `model_id`: (optional) Model to use (default: "scribe_v1")
- `language_code`: (optional) Language code (default: "eng")
- `diarize`: (optional) Whether to annotate speakers (default: true)
- `tag_audio_events`: (optional) Tag events like laughter (default: true)

**Response:**
```json
{
  "transcript": "Transcribed text here...",
  "model_used": "scribe_v1",
  "language": "eng"
}
```

### POST `/api/analyze-pitch`

Analyzes a pitch and returns comprehensive feedback.

**Request Body:**
```json
{
  "pitch_transcript": "Your pitch transcript here...",
  "context": {
    "audience": "investors",
    "goal": "raise funding",
    "duration": "1 minute"
  },
  "session_info": {
    "practice_attempt": 1,
    "wants_deploy_suggestions": true
  }
}
```

