from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QFileDialog, QWidget
import os
from tts_script import TTSBackend

class TTSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.tts_backend = TTSBackend()

    def initUI(self):
        self.setWindowTitle("TTS Frontend")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.label = QLabel("Enter text or drop a file:")
        layout.addWidget(self.label)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.file_button = QPushButton("Select Text File")
        self.file_button.clicked.connect(self.load_file)
        layout.addWidget(self.file_button)

        self.voice_label = QLabel("Select Voice:")
        layout.addWidget(self.voice_label)

        self.voice_selector = QComboBox()
        self.voice_selector.addItems(["tts_models/en/ljspeech/tacotron2-DDC", "tts_models/en/vctk/vits"])
        layout.addWidget(self.voice_selector)

        self.convert_button = QPushButton("Convert to Speech")
        self.convert_button.clicked.connect(self.convert_to_speech)
        layout.addWidget(self.convert_button)

        central_widget.setLayout(layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt)")
        if file_path:
            try:
                text = self.tts_backend.load_text_from_file(file_path)
                self.text_input.setText(text)
            except Exception as e:
                self.label.setText(f"Error: {e}")

    def convert_to_speech(self):
        text_to_speak = self.text_input.text()
        if not text_to_speak.strip():
            self.label.setText("Please provide text to convert.")
            return

        model_name = self.voice_selector.currentText()
        output_audio_path = os.path.expanduser("~/output.wav")

        try:
            self.tts_backend.generate_audio(text_to_speak, output_audio_path, model_name)
            self.label.setText(f"TTS finished! Saved to {output_audio_path}")
        except Exception as e:
            self.label.setText(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = TTSApp()
    window.show()
    app.exec_()