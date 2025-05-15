# mcp.py
from abc import ABC, abstractmethod
from typing import Dict
import os
import time
import requests
from dotenv import load_dotenv

class ModelContextProtocol(ABC):
    """Abstract base class for transcription engines."""
    @abstractmethod
    def transcribe(self, audio_path: str) -> Dict:
        """Given an audio file path, return transcription JSON."""
        ...

class AssemblyMCP(ModelContextProtocol):
    """AssemblyAI-based implementation."""
    def __init__(self, api_key: str = None):
        load_dotenv()
        self.api_key = api_key or os.getenv("ASSEMBLYAI_API_KEY")
        if not self.api_key:
            raise ValueError("Must set ASSEMBLYAI_API_KEY in .env or environment")
        self.headers = {
            "authorization": self.api_key,
            "content-type": "application/json"
        }
        self.base_url = "https://api.assemblyai.com/v2"

    def _upload(self, audio_path: str) -> str:
        """Upload file to AssemblyAI and return the upload URL."""
        with open(audio_path, "rb") as f:
            resp = requests.post(
                f"{self.base_url}/upload",
                headers={"authorization": self.api_key},
                data=f
            )
        resp.raise_for_status()
        return resp.json()["upload_url"]

    def transcribe(self, audio_path: str) -> Dict:
        """Submit transcription request, poll until complete, then return JSON."""
        upload_url = self._upload(audio_path)
        payload = {"audio_url": upload_url}
        resp = requests.post(
            f"{self.base_url}/transcript",
            headers=self.headers,
            json=payload
        )
        resp.raise_for_status()
        transcript_id = resp.json()["id"]

        while True:
            status_resp = requests.get(
                f"{self.base_url}/transcript/{transcript_id}",
                headers=self.headers
            )
            status_resp.raise_for_status()
            status_data = status_resp.json()
            if status_data["status"] in ("completed", "error"):
                return status_data
            time.sleep(1)