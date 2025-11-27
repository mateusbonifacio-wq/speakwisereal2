# SpeakWise Real

An AI-powered pitch and communication coach that helps users improve spoken pitches, introductions, and persuasive messages.

## Features

- **Comprehensive Pitch Analysis**: Get detailed feedback on clarity, structure, persuasiveness, storytelling, and more
- **Structured Feedback**: Receive actionable improvements organized into clear categories
- **Improved Pitch Rewrites**: Get a stronger version of your pitch that maintains your core message
- **Alternative Openings & Closings**: Multiple options to start and end your pitch effectively
- **Delivery Tips**: Voice, pace, and body language guidance
- **Practice Exercises**: Targeted exercises for your next attempt
- **Deploy Suggestions**: Help preparing your pitch for sharing (title, description, tags)

## Project Structure

```
speakwisereal2/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py      # API endpoints
│   │   ├── coach.py     # Core coaching logic
│   │   └── models.py    # Data models
│   ├── requirements.txt
│   └── .env.example
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.tsx
│   ├── package.json
│   └── tsconfig.json
└── README.md
```

## Quick Setup

For detailed setup instructions, see [SETUP.md](SETUP.md).

### Prerequisites
- Python 3.8+
- Node.js 16+ and npm
- Google API key for Gemini ([Get one here](https://makersuite.google.com/app/apikey))
- ElevenLabs API key for audio transcription ([Get one here](https://elevenlabs.io/app/settings/api-keys))

### Backend Setup

1. Navigate to backend and create virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_MODEL=gemini-pro
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

4. Run the server:
```bash
uvicorn app.main:app --reload
```

API available at `http://localhost:8000` | Docs at `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to frontend:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm start
```

Frontend available at `http://localhost:3000`

## API Endpoints

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
    "duration": "1 minute",
    "scenario": "startup investor pitch",
    "english_level": "fluent",
    "tone_style": "confident",
    "constraints": "no jargon",
    "notes_from_user": "this is my first attempt"
  },
  "session_info": {
    "practice_attempt": 1,
    "wants_deploy_suggestions": true
  }
}
```

**Response:**
Returns structured feedback following the exact format specified in the requirements.

## Usage

1. **Option A**: Upload an audio file to automatically transcribe it
2. **Option B**: Enter or paste your pitch transcript directly
3. Optionally provide context (audience, goal, duration, etc.)
4. Submit for analysis
5. Review the comprehensive feedback
6. Use the improved pitch and practice exercises for your next attempt

## Technology Stack

- **Backend**: FastAPI, Python, Google Gemini API, ElevenLabs API
- **Frontend**: React, TypeScript
- **AI**: Google Gemini models for pitch analysis
- **Audio Transcription**: ElevenLabs for speech-to-text conversion

## License

MIT

