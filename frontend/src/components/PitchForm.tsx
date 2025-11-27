import React, { useState } from 'react';
import './PitchForm.css';
import { PitchFormData } from '../types';

interface PitchFormProps {
  onSubmit: (data: PitchFormData) => void;
  loading: boolean;
}

const PitchForm: React.FC<PitchFormProps> = ({ onSubmit, loading }) => {
  const [pitchTranscript, setPitchTranscript] = useState('');
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [transcribing, setTranscribing] = useState(false);
  const [audioFile, setAudioFile] = useState<File | null>(null);
  
  // Context fields
  const [audience, setAudience] = useState('');
  const [goal, setGoal] = useState('');
  const [duration, setDuration] = useState('');
  const [scenario, setScenario] = useState('');
  const [englishLevel, setEnglishLevel] = useState('');
  const [toneStyle, setToneStyle] = useState('');
  const [constraints, setConstraints] = useState('');
  const [notesFromUser, setNotesFromUser] = useState('');
  
  // Session info
  const [practiceAttempt, setPracticeAttempt] = useState(1);
  const [wantsDeploySuggestions, setWantsDeploySuggestions] = useState(false);

  const handleAudioUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    // Validate file type
    const validTypes = ['audio/mpeg', 'audio/mp3', 'audio/wav', 'audio/m4a', 'audio/flac', 'audio/webm'];
    if (!validTypes.includes(file.type) && !file.name.match(/\.(mp3|wav|m4a|flac|webm)$/i)) {
      alert('Please upload a valid audio file (MP3, WAV, M4A, FLAC, or WEBM)');
      return;
    }

    setAudioFile(file);
    setTranscribing(true);

    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('model_id', 'scribe_v1');
      formData.append('language_code', 'eng');
      formData.append('diarize', 'true');
      formData.append('tag_audio_events', 'true');

      const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      const response = await fetch(`${API_BASE_URL}/api/transcribe-audio`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Transcription failed: ${response.statusText}`);
      }

      const data = await response.json();
      setPitchTranscript(data.transcript);
      setAudioFile(null);
    } catch (error) {
      alert(`Error transcribing audio: ${error instanceof Error ? error.message : 'Unknown error'}`);
    } finally {
      setTranscribing(false);
      // Reset file input
      e.target.value = '';
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!pitchTranscript.trim()) {
      alert('Please enter your pitch transcript or upload an audio file');
      return;
    }

    const formData: PitchFormData = {
      pitch_transcript: pitchTranscript,
    };

    // Add context if any field is filled
    const hasContext = audience || goal || duration || scenario || 
                      englishLevel || toneStyle || constraints || notesFromUser;
    
    if (hasContext) {
      formData.context = {};
      if (audience) formData.context.audience = audience;
      if (goal) formData.context.goal = goal;
      if (duration) formData.context.duration = duration;
      if (scenario) formData.context.scenario = scenario;
      if (englishLevel) formData.context.english_level = englishLevel;
      if (toneStyle) formData.context.tone_style = toneStyle;
      if (constraints) formData.context.constraints = constraints;
      if (notesFromUser) formData.context.notes_from_user = notesFromUser;
    }

    // Add session info
    formData.session_info = {
      practice_attempt: practiceAttempt,
      wants_deploy_suggestions: wantsDeploySuggestions,
    };

    onSubmit(formData);
  };

  return (
    <form className="pitch-form" onSubmit={handleSubmit}>
      <div className="form-section">
        <label htmlFor="pitch-transcript">
          <h2>Your Pitch Transcript *</h2>
          <p className="label-hint">
            Paste or type your pitch transcript here. It can include filler words, repetitions, or minor errors.
          </p>
        </label>
        <textarea
          id="pitch-transcript"
          value={pitchTranscript}
          onChange={(e) => setPitchTranscript(e.target.value)}
          placeholder="Enter your pitch transcript here..."
          rows={10}
          required
        />
      </div>

      <div className="form-section">
        <button
          type="button"
          className="toggle-advanced"
          onClick={() => setShowAdvanced(!showAdvanced)}
        >
          {showAdvanced ? '▼' : '▶'} Advanced Options (Optional)
        </button>
      </div>

      {showAdvanced && (
        <div className="advanced-options">
          <div className="form-section">
            <h3>Context</h3>
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="audience">Audience</label>
                <input
                  type="text"
                  id="audience"
                  value={audience}
                  onChange={(e) => setAudience(e.target.value)}
                  placeholder="e.g., investors, hiring manager, customers"
                />
              </div>

              <div className="form-group">
                <label htmlFor="goal">Goal</label>
                <input
                  type="text"
                  id="goal"
                  value={goal}
                  onChange={(e) => setGoal(e.target.value)}
                  placeholder="e.g., raise funding, get hired, book a meeting"
                />
              </div>

              <div className="form-group">
                <label htmlFor="duration">Duration</label>
                <select
                  id="duration"
                  value={duration}
                  onChange={(e) => setDuration(e.target.value)}
                >
                  <option value="">Select duration...</option>
                  <option value="30 seconds">30 seconds</option>
                  <option value="1 minute">1 minute</option>
                  <option value="2 minutes">2 minutes</option>
                  <option value="3 minutes">3 minutes</option>
                  <option value="5 minutes">5 minutes</option>
                  <option value="elevator pitch">Elevator pitch</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="scenario">Scenario</label>
                <input
                  type="text"
                  id="scenario"
                  value={scenario}
                  onChange={(e) => setScenario(e.target.value)}
                  placeholder="e.g., startup investor pitch, job interview"
                />
              </div>

              <div className="form-group">
                <label htmlFor="english-level">English Level</label>
                <select
                  id="english-level"
                  value={englishLevel}
                  onChange={(e) => setEnglishLevel(e.target.value)}
                >
                  <option value="">Select level...</option>
                  <option value="beginner">Beginner</option>
                  <option value="intermediate">Intermediate</option>
                  <option value="advanced">Advanced</option>
                  <option value="fluent">Fluent</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="tone-style">Tone/Style</label>
                <select
                  id="tone-style"
                  value={toneStyle}
                  onChange={(e) => setToneStyle(e.target.value)}
                >
                  <option value="">Select tone...</option>
                  <option value="confident">Confident</option>
                  <option value="friendly">Friendly</option>
                  <option value="inspiring">Inspiring</option>
                  <option value="professional">Professional</option>
                  <option value="casual">Casual</option>
                  <option value="humorous">Humorous</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="constraints">Constraints</label>
              <input
                type="text"
                id="constraints"
                value={constraints}
                onChange={(e) => setConstraints(e.target.value)}
                placeholder="e.g., no jargon, max 1 minute, keep it simple"
              />
            </div>

            <div className="form-group">
              <label htmlFor="notes-from-user">Notes from You</label>
              <textarea
                id="notes-from-user"
                value={notesFromUser}
                onChange={(e) => setNotesFromUser(e.target.value)}
                placeholder="e.g., this is my first attempt, I'm nervous, I want something punchy"
                rows={3}
              />
            </div>
          </div>

          <div className="form-section">
            <h3>Session Info</h3>
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="practice-attempt">Practice Attempt</label>
                <input
                  type="number"
                  id="practice-attempt"
                  value={practiceAttempt}
                  onChange={(e) => setPracticeAttempt(parseInt(e.target.value) || 1)}
                  min={1}
                />
              </div>

              <div className="form-group checkbox-group">
                <label>
                  <input
                    type="checkbox"
                    checked={wantsDeploySuggestions}
                    onChange={(e) => setWantsDeploySuggestions(e.target.checked)}
                  />
                  Include deploy/sharing suggestions
                </label>
              </div>
            </div>
          </div>
        </div>
      )}

      <div className="form-section">
        <button type="submit" className="submit-button" disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze Pitch'}
        </button>
      </div>
    </form>
  );
};

export default PitchForm;

