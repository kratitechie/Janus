from pathlib import Path

from src.media.voice_processor import VoiceProcessor

processor = VoiceProcessor()

processor.extract(
    Path("dataset/media/audio/vn_007.mp3")
)

print("DONE")