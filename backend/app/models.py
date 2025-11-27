from pydantic import BaseModel, Field
from typing import Optional


class TranscriptionResponse(BaseModel):
    transcript: str = Field(..., description="Transcribed text from audio")
    model_used: str = Field(..., description="Model used for transcription")
    language: str = Field(..., description="Language code used")


class Context(BaseModel):
    audience: Optional[str] = None
    goal: Optional[str] = None
    duration: Optional[str] = None
    scenario: Optional[str] = None
    english_level: Optional[str] = None
    tone_style: Optional[str] = None
    constraints: Optional[str] = None
    notes_from_user: Optional[str] = None


class SessionInfo(BaseModel):
    practice_attempt: Optional[int] = Field(default=1, ge=1)
    wants_deploy_suggestions: Optional[bool] = Field(default=False)


class PitchAnalysisRequest(BaseModel):
    pitch_transcript: str = Field(..., min_length=1, description="Transcript of the spoken pitch")
    context: Optional[Context] = None
    session_info: Optional[SessionInfo] = None


class Score(BaseModel):
    value: int = Field(..., ge=0, le=10, description="Score from 0-10")
    reason: str = Field(..., description="One sentence explanation")


class Scores(BaseModel):
    clarity: Score
    structure_flow: Score
    persuasiveness: Score
    storytelling_examples: Score
    conciseness_vs_duration: Score
    fit_for_audience_goal: Score
    delivery_energy: Score


class PitchAnalysisResponse(BaseModel):
    quick_summary: str
    scores: Scores
    context_check: str
    what_you_did_well: list[str]
    what_to_improve: list[str]
    improved_pitch: str
    alternative_openings: list[str]
    alternative_closings: list[str]
    delivery_tips: list[str]
    next_practice_exercise: str
    deploy_suggestions: Optional[dict] = None

