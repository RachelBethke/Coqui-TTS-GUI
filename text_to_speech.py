import os
from TTS.api import TTS

txt_file_path = "/Users/rachelbethke/IdeaProjects/tts_stuff/test.txt"
output_audio_path = "/Users/rachelbethke/IdeaProjects/tts_stuff/output.wav"

model_name = "tts_models/en/ljspeech/tacotron2-DDC"

if not os.path.exists(txt_file_path):
    raise FileNotFoundError(f"Text file not found: {txt_file_path}")

try:
    with open(txt_file_path, "r", encoding="utf-8") as file:
        text_to_speak = file.read().strip()
except UnicodeDecodeError:
    print("UTF-8 failed. Trying ISO-8859-1 encoding")
    with open(txt_file_path, "r", encoding="ISO-8859-1") as file:
        text_to_speak = file.read().strip()

tts = TTS(model_name=model_name)
tts.tts_to_file(text=text_to_speak, file_path=output_audio_path)

print(f"TTS finished")
