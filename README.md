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
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

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

3. Create `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4-turbo-preview
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

1. Enter or paste your pitch transcript
2. Optionally provide context (audience, goal, duration, etc.)
3. Submit for analysis
4. Review the comprehensive feedback
5. Use the improved pitch and practice exercises for your next attempt

## Technology Stack

- **Backend**: FastAPI, Python, OpenAI API
- **Frontend**: React, TypeScript
- **AI**: OpenAI GPT models for pitch analysis

## License

MIT

