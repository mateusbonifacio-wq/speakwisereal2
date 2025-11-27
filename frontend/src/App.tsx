import React, { useState } from 'react';
import './App.css';
import PitchForm from './components/PitchForm';
import FeedbackDisplay from './components/FeedbackDisplay';
import { PitchAnalysisResponse } from './types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [feedback, setFeedback] = useState<PitchAnalysisResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (formData: any) => {
    setLoading(true);
    setError(null);
    setFeedback(null);

    try {
      const response = await fetch(`${API_BASE_URL}/api/analyze-pitch`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
      }

      const data = await response.json();
      setFeedback(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>SpeakWise Real</h1>
        <p className="subtitle">AI-Powered Pitch & Communication Coach</p>
      </header>

      <main className="App-main">
        <div className="container">
          <PitchForm onSubmit={handleSubmit} loading={loading} />
          
          {error && (
            <div className="error-message">
              <strong>Error:</strong> {error}
            </div>
          )}

          {feedback && <FeedbackDisplay feedback={feedback} />}
        </div>
      </main>
    </div>
  );
}

export default App;

