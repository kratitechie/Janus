import os
import json
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError


ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env", override=True)


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-3.6-flash"

    def _generate(self, **kwargs):

        retries = 5

        for attempt in range(retries):

            try:

                return self.client.models.generate_content(**kwargs)

            except ClientError as e:

                if e.status_code == 429:

                    wait = 40

                    print(f"\n[RATE LIMIT] Waiting {wait}s...\n")

                    time.sleep(wait)

                    continue

                raise

        raise RuntimeError("Maximum retries exceeded.")

    def generate(self, prompt: str):

        response = self._generate(

            model=self.model,

            contents=prompt

        )

        return response.text

    def generate_json(self, prompt: str):

        response = self._generate(

            model=self.model,

            contents=prompt,

            config={

                "response_mime_type": "application/json"

            }

        )

        return json.loads(response.text)