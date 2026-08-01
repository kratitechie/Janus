from pathlib import Path

from google.genai import types

from src.llm.gemini_client import GeminiClient


class VoiceProcessor:

    def __init__(self):

        self.client = GeminiClient()

        self.cache = Path("cache/audio")

        self.cache.mkdir(parents=True, exist_ok=True)

    def extract(self, audio_path):

        audio = Path(audio_path)

        cache_file = self.cache / f"{audio.stem}.txt"

        # ---------- CACHE ----------

        if cache_file.exists():

            print(f"[CACHE] {audio.stem}")

            return cache_file.read_text(
                encoding="utf-8"
            )

        # ---------- GEMINI ----------

        response = self.client.client.models.generate_content(

            model=self.client.model,

            contents=[

                types.Part.from_bytes(
                    data=audio.read_bytes(),
                    mime_type="audio/mpeg"
                ),

                """
Transcribe this voice note.

Return only the spoken words.

Do not summarize.
"""

            ]

        )

        text = response.text.strip()

        cache_file.write_text(
            text,
            encoding="utf-8"
        )

        return text