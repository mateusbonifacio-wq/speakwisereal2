export interface Score {
  value: number;
  reason: string;
}

export interface Scores {
  clarity: Score;
  structure_flow: Score;
  persuasiveness: Score;
  storytelling_examples: Score;
  conciseness_vs_duration: Score;
  fit_for_audience_goal: Score;
  delivery_energy: Score;
}

export interface PitchAnalysisResponse {
  quick_summary: string;
  scores: Scores;
  context_check: string;
  what_you_did_well: string[];
  what_to_improve: string[];
  improved_pitch: string;
  alternative_openings: string[];
  alternative_closings: string[];
  delivery_tips: string[];
  next_practice_exercise: string;
  deploy_suggestions?: {
    title: string;
    description: string;
    tags: string[];
  };
}

export interface Context {
  audience?: string;
  goal?: string;
  duration?: string;
  scenario?: string;
  english_level?: string;
  tone_style?: string;
  constraints?: string;
  notes_from_user?: string;
}

export interface SessionInfo {
  practice_attempt?: number;
  wants_deploy_suggestions?: boolean;
}

export interface PitchFormData {
  pitch_transcript: string;
  context?: Context;
  session_info?: SessionInfo;
}

