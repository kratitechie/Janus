import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

class EmbeddingClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def embed(self, text: str):

        response = self.client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values