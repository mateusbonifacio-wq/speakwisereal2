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

4. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4-turbo-preview
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

