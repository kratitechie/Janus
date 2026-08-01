import os
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# -----------------------------
# Load Environment Variables
# -----------------------------
ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env", override=True)


class GeminiClient:
    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

        # We'll use this everywhere in JANUS
        self.model = "gemini-3.6-flash"

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text

    def generate_json(self, prompt: str) -> dict:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        return json.loads(response.text)