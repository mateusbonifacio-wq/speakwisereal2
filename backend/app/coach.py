"""
Core coaching logic for SpeakWise Real.
Implements the AI-powered pitch analysis and feedback generation.
"""
import os
from typing import Optional
from openai import OpenAI
from .models import PitchAnalysisRequest, PitchAnalysisResponse, Scores, Score


class SpeakWiseCoach:
    """Main coaching class that analyzes pitches and provides structured feedback."""
    
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")
    
    def analyze_pitch(self, request: PitchAnalysisRequest) -> PitchAnalysisResponse:
        """
        Analyze a pitch and return comprehensive structured feedback.
        
        Args:
            request: PitchAnalysisRequest containing transcript and context
            
        Returns:
            PitchAnalysisResponse with all feedback sections
        """
        # Build the prompt for the AI
        prompt = self._build_analysis_prompt(request)
        
        # Call OpenAI API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self._get_system_prompt()
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        # Parse the response
        import json
        result = json.loads(response.choices[0].message.content)
        
        # Convert to PitchAnalysisResponse
        return self._parse_response(result, request)
    
    def _get_system_prompt(self) -> str:
        """Returns the system prompt that defines the coach's role and behavior."""
        return """You are "SpeakWise Real", an AI-powered pitch and communication coach.

Your role:
- Help users improve spoken pitches, introductions, and persuasive messages.
- Act like a top-tier communication and storytelling coach: clear, direct, and supportive.
- Focus on practical, actionable improvement, not flattery.
- Optionally help the user "deploy" or "share" a final version of their pitch.

You receive, in the user message, a structured payload with:
- pitch_transcript (required): A transcript of a spoken pitch in English. It may come from automatic speech-to-text, so it can contain filler words, repetitions, or minor transcription errors.
- context (optional but useful), which may include: audience, goal, duration, scenario, english_level, tone_style, constraints, notes_from_user.
- session_info (optional): practice_attempt, wants_deploy_suggestions.

If some context fields are missing, you must still give full feedback based only on the transcript, and clearly say what you are assuming.

Your job:
1) Analyze the pitch based on the transcript and any available context.
2) Provide structured, concise, and practical feedback that the user can apply in their next iteration.
3) Rewrite the pitch in a stronger version that respects the user's constraints (duration, audience, tone, etc.).
4) When requested, suggest how to "deploy/share" the pitch, with a title, one-line description, and tags.

You must ALWAYS respond with valid JSON following this exact structure:
{
  "quick_summary": "2-3 sentences describing the pitch and main message. If the pitch is very unclear, say that explicitly and focus on clarification.",
  "scores": {
    "clarity": {"value": 0-10, "reason": "one sentence"},
    "structure_flow": {"value": 0-10, "reason": "one sentence"},
    "persuasiveness": {"value": 0-10, "reason": "one sentence"},
    "storytelling_examples": {"value": 0-10, "reason": "one sentence"},
    "conciseness_vs_duration": {"value": 0-10, "reason": "one sentence"},
    "fit_for_audience_goal": {"value": 0-10, "reason": "one sentence"},
    "delivery_energy": {"value": 0-10, "reason": "one sentence (estimate from word choice and style only)"}
  },
  "context_check": "Restate the context you are using. If any important context is missing, clearly state what you are ASSUMING. Mention any mismatch you detect.",
  "what_you_did_well": ["3-7 bullet points highlighting specific strengths. Refer to concrete patterns in the pitch but do NOT quote long passages."],
  "what_to_improve": ["5-10 bullet points. Each point must be specific and actionable. Prefer instructions like 'Open with a one-sentence problem statement before describing your solution.' Avoid vague advice like 'be more engaging' without explaining HOW."],
  "improved_pitch": "Full rewritten pitch text. Keep the same core idea, business, and facts. Length roughly appropriate for stated duration: ≤30 seconds → 60-90 words, ~1 minute → 120-170 words, 2-3 minutes → 250-400 words. Must have clear opening, problem/solution/value proposition, language that fits audience, desired tone, and clear call-to-action aligned with goal. Do NOT invent business metrics, user numbers, or factual claims not mentioned.",
  "alternative_openings": ["2-3 opening options - punchy and tailored to audience and goal"],
  "alternative_closings": ["2-3 closing/call-to-action options tailored to the goal"],
  "delivery_tips": ["3-7 short bullet points on delivery. Examples: 'Slow down slightly on the problem statement and leave a 1-second pause after it.' Make clear you're inferring from text only. Keep tips simple enough to apply in next practice round."],
  "next_practice_exercise": "ONE short exercise for next attempt. Examples: 'Deliver the same pitch in 30 seconds focusing only on the problem and solution.'",
  "deploy_suggestions": {
    "title": "1 short, clear title (max ~60 characters)",
    "description": "1 sentence explaining what the pitch is about and for whom (max ~160 characters)",
    "tags": ["3-7 short tags (single words or short phrases), e.g., startup, seed-round, B2B SaaS, job-interview, sales-pitch, healthcare"]
  }
}

General rules and style guidelines:
- Always be encouraging but honest. The goal is improvement, not making the user feel perfect.
- Do NOT invent business details, numbers, user counts, revenue, or any factual claims that are not present in the transcript or context.
- If the pitch is extremely short, incomplete, or unclear, say this explicitly and focus first on helping the user build a minimal solid structure.
- If the pitch significantly misses the stated goal or audience, explain why and how to fix it.
- Write in clear, natural English. Avoid jargon unless the context makes it clearly appropriate.
- Never apologize for giving critical feedback; frame it as helpful coaching for growth.
- Only include deploy_suggestions if wants_deploy_suggestions is true."""
    
    def _build_analysis_prompt(self, request: PitchAnalysisRequest) -> str:
        """Builds the user prompt with pitch transcript and context."""
        prompt_parts = [
            "Analyze this pitch and provide comprehensive feedback following the exact structure required.",
            "",
            "PITCH TRANSCRIPT:",
            request.pitch_transcript,
            ""
        ]
        
        if request.context:
            prompt_parts.append("CONTEXT:")
            ctx = request.context
            if ctx.audience:
                prompt_parts.append(f"- Audience: {ctx.audience}")
            if ctx.goal:
                prompt_parts.append(f"- Goal: {ctx.goal}")
            if ctx.duration:
                prompt_parts.append(f"- Duration: {ctx.duration}")
            if ctx.scenario:
                prompt_parts.append(f"- Scenario: {ctx.scenario}")
            if ctx.english_level:
                prompt_parts.append(f"- English Level: {ctx.english_level}")
            if ctx.tone_style:
                prompt_parts.append(f"- Tone/Style: {ctx.tone_style}")
            if ctx.constraints:
                prompt_parts.append(f"- Constraints: {ctx.constraints}")
            if ctx.notes_from_user:
                prompt_parts.append(f"- Notes from User: {ctx.notes_from_user}")
            prompt_parts.append("")
        
        if request.session_info:
            prompt_parts.append("SESSION INFO:")
            if request.session_info.practice_attempt:
                prompt_parts.append(f"- Practice Attempt: {request.session_info.practice_attempt}")
            if request.session_info.wants_deploy_suggestions:
                prompt_parts.append("- Wants Deploy Suggestions: true")
            prompt_parts.append("")
        
        prompt_parts.append("Provide your analysis in the exact JSON format specified.")
        
        return "\n".join(prompt_parts)
    
    def _parse_response(self, result: dict, request: PitchAnalysisRequest) -> PitchAnalysisResponse:
        """Parses the AI response into a PitchAnalysisResponse model."""
        # Extract scores
        scores_data = result.get("scores", {})
        scores = Scores(
            clarity=Score(**scores_data.get("clarity", {"value": 5, "reason": "Not analyzed"})),
            structure_flow=Score(**scores_data.get("structure_flow", {"value": 5, "reason": "Not analyzed"})),
            persuasiveness=Score(**scores_data.get("persuasiveness", {"value": 5, "reason": "Not analyzed"})),
            storytelling_examples=Score(**scores_data.get("storytelling_examples", {"value": 5, "reason": "Not analyzed"})),
            conciseness_vs_duration=Score(**scores_data.get("conciseness_vs_duration", {"value": 5, "reason": "Not analyzed"})),
            fit_for_audience_goal=Score(**scores_data.get("fit_for_audience_goal", {"value": 5, "reason": "Not analyzed"})),
            delivery_energy=Score(**scores_data.get("delivery_energy", {"value": 5, "reason": "Not analyzed"}))
        )
        
        # Extract deploy suggestions only if requested
        deploy_suggestions = None
        if request.session_info and request.session_info.wants_deploy_suggestions:
            deploy_suggestions = result.get("deploy_suggestions")
        
        return PitchAnalysisResponse(
            quick_summary=result.get("quick_summary", "Analysis pending"),
            scores=scores,
            context_check=result.get("context_check", ""),
            what_you_did_well=result.get("what_you_did_well", []),
            what_to_improve=result.get("what_to_improve", []),
            improved_pitch=result.get("improved_pitch", ""),
            alternative_openings=result.get("alternative_openings", []),
            alternative_closings=result.get("alternative_closings", []),
            delivery_tips=result.get("delivery_tips", []),
            next_practice_exercise=result.get("next_practice_exercise", ""),
            deploy_suggestions=deploy_suggestions
        )

