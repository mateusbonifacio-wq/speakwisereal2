"""
Audio transcription service using ElevenLabs API.
"""
import os
from io import BytesIO
from typing import Optional
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()


class TranscriptionService:
    """Service for transcribing audio files using ElevenLabs."""
    
    def __init__(self):
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key:
            raise ValueError("ELEVENLABS_API_KEY environment variable is not set")
        
        self.client = ElevenLabs(api_key=api_key)
    
    def transcribe_audio(
        self,
        audio_file: bytes,
        model_id: str = "scribe_v1",
        language_code: str = "eng",
        diarize: bool = True,
        tag_audio_events: bool = True
    ) -> str:
        """
        Transcribe an audio file to text.
        
        Args:
            audio_file: Audio file bytes
            model_id: Model to use (default: "scribe_v1")
            language_code: Language of the audio file (default: "eng")
            diarize: Whether to annotate who is speaking (default: True)
            tag_audio_events: Tag audio events like laughter, applause, etc. (default: True)
            
        Returns:
            Transcribed text as string
        """
        # Convert bytes to BytesIO
        audio_data = BytesIO(audio_file)
        
        # Transcribe using ElevenLabs
        transcription = self.client.speech_to_text.convert(
            file=audio_data,
            model_id=model_id,
            tag_audio_events=tag_audio_events,
            language_code=language_code,
            diarize=diarize,
        )
        
        return transcription

