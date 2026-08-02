from pathlib import Path

from src.loaders.data_loader import DataLoader
from src.media.image_processor import ImageProcessor
from src.media.voice_processor import VoiceProcessor


DATASET_ROOT = Path("dataset").resolve()


loader = DataLoader()

image_processor = ImageProcessor()

voice_processor = VoiceProcessor()


# ---------------- Images ----------------

print("\n========== CACHING IMAGES ==========\n")

for _, row in loader.images.iterrows():

    image_path = DATASET_ROOT / row["file_path"]

    print(f"Image: {row['image_id']}")

    try:

        image_processor.extract(image_path)

    except Exception as e:

        print(e)
        break


# ---------------- Voice ----------------

print("\n========== CACHING VOICE ==========\n")

for _, row in loader.voice_notes.iterrows():

    audio_path = DATASET_ROOT / row["file_path"]

    print(f"Voice: {row['voice_note_id']}")

    try:

        voice_processor.extract(audio_path)

    except Exception as e:
        print(e)
        break


print("\nDONE")