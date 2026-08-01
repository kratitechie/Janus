from pathlib import Path

from google.genai import types

from src.llm.gemini_client import GeminiClient


class ImageProcessor:

    def __init__(self):

        self.client = GeminiClient()

        self.cache = Path("cache/ocr")

        self.cache.mkdir(parents=True, exist_ok=True)

    def extract(self, image_path):

        image = Path(image_path)

        cache_file = self.cache / f"{image.stem}.txt"

        # ---------- CACHE ----------

        if cache_file.exists():

            print(f"[CACHE] {image.stem}")

            return cache_file.read_text(
                encoding="utf-8"
            )

        # ---------- GEMINI ----------

        response = self.client.client.models.generate_content(

            model=self.client.model,

            contents=[

                types.Part.from_bytes(
                    data=image.read_bytes(),
                    mime_type="image/jpeg"
                ),

                """
Analyze this WhatsApp image.

If the image contains readable text,
extract ALL important text.

If it is a poster,
extract:
- event
- date
- time
- location
- urgency
- action required

If it is a screenshot,
extract the visible information.

If it is a normal photograph,
briefly describe what is happening.

Return only plain text.
"""

            ]

        )

        text = response.text.strip()

        cache_file.write_text(
            text,
            encoding="utf-8"
        )

        return text