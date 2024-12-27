import os
from TTS.api import TTS

class TTSBackend:
    def __init__(self):
        self.tts_instances = {}  # Cache models for reuse

    def generate_audio(self, text, output_audio_path, model_name="tts_models/en/ljspeech/tacotron2-DDC"):
        """Generate audio from the given text using the specified TTS model."""
        if model_name not in self.tts_instances:
            print(f"Loading model: {model_name}")
            self.tts_instances[model_name] = TTS(model_name=model_name)
        tts = self.tts_instances[model_name]
        print(f"Generating audio...")
        tts.tts_to_file(text=text, file_path=output_audio_path)
        print(f"Audio saved to: {output_audio_path}")

    def load_text_from_file(self, file_path):
        """Read text from a file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Text file not found: {file_path}")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read().strip()
        except UnicodeDecodeError:
            with open(file_path, "r", encoding="ISO-8859-1") as file:
                return file.read().strip()
