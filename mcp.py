# mcp.py
from typing import Protocol, Dict
import whisper

class ModelContextProtocol(Protocol):
    """Protocol for any model-based transcription service."""
    def transcribe(self, audio_path: str) -> Dict:
        ...

class WhisperMCP:
    """Whisper-based implementation of ModelContextProtocol."""
    def __init__(self, model_name: str = "base"):
        # load the Whisper model once
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str) -> Dict:
        # run the transcription and return the dict it gives you
        return self.model.transcribe(audio_path)
