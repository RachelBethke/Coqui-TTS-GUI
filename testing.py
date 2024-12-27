from TTS.api import TTS

# Create an instance of TTS
tts = TTS(model_name=None)

# List available TTS models
models = tts.list_models().list_tts_models()  # Use the list_tts_models method
print("Available TTS models:")
for model in models:
    print(f"- {model}")
