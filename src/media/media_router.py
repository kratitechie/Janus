from pathlib import Path

from src.media.image_processor import ImageProcessor
from src.media.voice_processor import VoiceProcessor

DATASET_ROOT = Path("dataset").resolve()

class MediaRouter:

    def __init__(self, loader):

        self.loader = loader

        self.image = ImageProcessor()

        self.voice = VoiceProcessor()

    def process(self, message):

        media_type = message["media_type"]

        if media_type == "image":

            row = self.loader.images[
                self.loader.images["image_id"] == message["media_id"]
            ].iloc[0]

            image_path = DATASET_ROOT / row["file_path"]

            return self.image.extract(image_path)

        elif media_type == "voice":

            row = self.loader.voice_notes[
                self.loader.voice_notes["voice_note_id"] == message["media_id"]
            ].iloc[0]

            audio_path = DATASET_ROOT / row["file_path"]

            return self.voice.extract(audio_path)
                
        return message["message_text"]