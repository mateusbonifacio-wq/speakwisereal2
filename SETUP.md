# SpeakWise Real - Setup Guide

## Quick Start

### Prerequisites
- Python 3.8+ 
- Node.js 16+ and npm
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the `backend` directory:
```bash
# Windows
type nul > .env

# Mac/Linux
touch .env
```

5. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4-turbo-preview
```

6. Run the backend server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. (Optional) Create a `.env` file if you need to change the API URL:
```
REACT_APP_API_URL=http://localhost:8000
```

4. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## Usage

1. Open `http://localhost:3000` in your browser
2. Enter or paste your pitch transcript
3. Optionally fill in context fields (audience, goal, duration, etc.)
4. Click "Analyze Pitch"
5. Review the comprehensive feedback

## Troubleshooting

### Backend Issues

- **"OPENAI_API_KEY environment variable is not set"**: Make sure you created the `.env` file in the `backend` directory and added your API key
- **Import errors**: Make sure you activated your virtual environment and installed all requirements
- **Port already in use**: Change the port in `uvicorn app.main:app --reload --port 8001`

### Frontend Issues

- **Cannot connect to API**: Make sure the backend is running on port 8000, or update `REACT_APP_API_URL` in frontend `.env`
- **npm install fails**: Try deleting `node_modules` and `package-lock.json`, then run `npm install` again

## Production Deployment

### Backend
- Use a production ASGI server like Gunicorn with Uvicorn workers
- Set up proper environment variables
- Configure CORS for your frontend domain

### Frontend
- Run `npm run build` to create a production build
- Serve the `build/` directory with a static file server
- Update `REACT_APP_API_URL` to point to your production API

