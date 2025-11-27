import React from 'react';
import './FeedbackDisplay.css';
import { PitchAnalysisResponse } from '../types';

interface FeedbackDisplayProps {
  feedback: PitchAnalysisResponse;
}

const FeedbackDisplay: React.FC<FeedbackDisplayProps> = ({ feedback }) => {
  const getScoreColor = (score: number): string => {
    if (score >= 8) return '#4caf50';
    if (score >= 6) return '#ff9800';
    return '#f44336';
  };

  return (
    <div className="feedback-display">
      <h2 className="feedback-title">Your Pitch Analysis</h2>

      {/* Quick Summary */}
      <section className="feedback-section">
        <h3>1. Quick Summary</h3>
        <p className="summary-text">{feedback.quick_summary}</p>
      </section>

      {/* Scores */}
      <section className="feedback-section">
        <h3>2. Scores (0–10)</h3>
        <div className="scores-grid">
          <div className="score-item">
            <div className="score-header">
              <span className="score-label">Clarity</span>
              <span 
                className="score-value" 
                style={{ color: getScoreColor(feedback.scores.clarity.value) }}
              >
                {feedback.scores.clarity.value}/10
              </span>
            </div>
            <p className="score-reason">{feedback.scores.clarity.reason}</p>
          </div>

          <div className="score-item">
            <div className="score-header">
              <span className="score-label">Structure & Flow</span>
              <span 
                className="score-value" 
                style={{ color: getScoreColor(feedback.scores.structure_flow.value) }}
              >
                {feedback.scores.structure_flow.value}/10
              </span>
            </div>
            <p className="score-reason">{feedback.scores.structure_flow.reason}</p>
          </div>

          <div className="score-item">
            <div className="score-header">
              <span className="score-label">Persuasiveness</span>
              <span 
                className="score-value" 
                style={{ color: getScoreColor(feedback.scores.persuasiveness.value) }}
              >
                {feedback.scores.persuasiveness.value}/10
              </span>
            </div>
            <p className="score-reason">{feedback.scores.persuasiveness.reason}</p>
          </div>

          <div className="score-item">
            <div className="score-header">
              <span className="score-label">Storytelling & Examples</span>
              <span 
                className="score-value" 
                style={{ color: getScoreColor(feedback.scores.storytelling_examples.value) }}
              >
                {feedback.scores.storytelling_examples.value}/10
              </span>
            </div>
            <p className="score-reason">{feedback.scores.storytelling_examples.reason}</p>
          </div>

          <div className="score-item">
            <div className="score-header">
              <span className="score-label">Conciseness vs. Duration</span>
              <span 
                className="score-value" 
                style={{ color: getScoreColor(feedback.scores.conciseness_vs_duration.value) }}
              >
                {feedback.scores.conciseness_vs_duration.value}/10
              </span>
            </div>
            <p className="score-reason">{feedback.scores.conciseness_vs_duration.reason}</p>
          </div>

          <div className="score-item">
            <div className="score-header">
              <span className="score-label">Fit for Audience & Goal</span>
              <span 
                className="score-value" 
                style={{ color: getScoreColor(feedback.scores.fit_for_audience_goal.value) }}
              >
                {feedback.scores.fit_for_audience_goal.value}/10
              </span>
            </div>
            <p className="score-reason">{feedback.scores.fit_for_audience_goal.reason}</p>
          </div>

          <div className="score-item">
            <div className="score-header">
              <span className="score-label">Delivery & Energy</span>
              <span 
                className="score-value" 
                style={{ color: getScoreColor(feedback.scores.delivery_energy.value) }}
              >
                {feedback.scores.delivery_energy.value}/10
              </span>
            </div>
            <p className="score-reason">{feedback.scores.delivery_energy.reason}</p>
          </div>
        </div>
      </section>

      {/* Context Check */}
      <section className="feedback-section">
        <h3>3. Context Check</h3>
        <div className="context-text">{feedback.context_check}</div>
      </section>

      {/* What You Did Well */}
      <section className="feedback-section">
        <h3>4. What You Did Well</h3>
        <ul className="feedback-list positive">
          {feedback.what_you_did_well.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </section>

      {/* What to Improve */}
      <section className="feedback-section">
        <h3>5. What to Improve (Actionable)</h3>
        <ul className="feedback-list improvement">
          {feedback.what_to_improve.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </section>

      {/* Improved Pitch */}
      <section className="feedback-section">
        <h3>6. Improved Pitch (Same Idea, Stronger Version)</h3>
        <div className="improved-pitch">
          {feedback.improved_pitch}
        </div>
      </section>

      {/* Alternative Openings & Closings */}
      <section className="feedback-section">
        <h3>7. Alternative Openings & Closings</h3>
        <div className="alternatives-grid">
          <div>
            <h4>Opening Options:</h4>
            <ul className="alternatives-list">
              {feedback.alternative_openings.map((opening, index) => (
                <li key={index} className="alternative-item">{opening}</li>
              ))}
            </ul>
          </div>
          <div>
            <h4>Closing / Call-to-Action Options:</h4>
            <ul className="alternatives-list">
              {feedback.alternative_closings.map((closing, index) => (
                <li key={index} className="alternative-item">{closing}</li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* Delivery Tips */}
      <section className="feedback-section">
        <h3>8. Delivery Tips (Voice, Pace, Body Language)</h3>
        <ul className="feedback-list tips">
          {feedback.delivery_tips.map((tip, index) => (
            <li key={index}>{tip}</li>
          ))}
        </ul>
      </section>

      {/* Next Practice Exercise */}
      <section className="feedback-section">
        <h3>9. Next Practice Exercise</h3>
        <div className="practice-exercise">
          {feedback.next_practice_exercise}
        </div>
      </section>

      {/* Deploy Suggestions */}
      {feedback.deploy_suggestions && (
        <section className="feedback-section">
          <h3>10. Deploy / Sharing Suggestions</h3>
          <div className="deploy-suggestions">
            <div className="deploy-item">
              <strong>Title for the Pitch Page:</strong>
              <p>{feedback.deploy_suggestions.title}</p>
            </div>
            <div className="deploy-item">
              <strong>One-Line Description:</strong>
              <p>{feedback.deploy_suggestions.description}</p>
            </div>
            <div className="deploy-item">
              <strong>Tags:</strong>
              <div className="tags">
                {feedback.deploy_suggestions.tags.map((tag, index) => (
                  <span key={index} className="tag">{tag}</span>
                ))}
              </div>
            </div>
          </div>
        </section>
      )}
    </div>
  );
};

export default FeedbackDisplay;

