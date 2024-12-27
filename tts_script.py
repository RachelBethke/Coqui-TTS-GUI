import os
from TTS.api import TTS

class TTSBackend:
    def __init__(self):
        self.tts_instances = {}  # Cache loaded models

    def generate_audio(self, text, output_audio_path, model_name):
        # Expand ~ to the user's home directory
        output_audio_path = os.path.expanduser(output_audio_path)

        if model_name not in self.tts_instances:
            print(f"Loading model: {model_name}")
            self.tts_instances[model_name] = TTS(model_name=model_name)
        tts = self.tts_instances[model_name]
        print("Generating audio...")
        tts.tts_to_file(text=text, file_path=output_audio_path)
        print(f"Audio saved to: {output_audio_path}")