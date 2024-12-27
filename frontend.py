from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QFileDialog, QWidget
from tts_script import TTSBackend

class TTSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.tts_backend = TTSBackend()
        self.output_audio_path = None  # Path to save the audio file

    def initUI(self):
        self.setWindowTitle("TTS Frontend")
        self.setGeometry(100, 100, 400, 350)

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

        self.save_button = QPushButton("Set Output File")
        self.save_button.clicked.connect(self.save_file_dialog)
        layout.addWidget(self.save_button)

        self.convert_button = QPushButton("Convert to Speech")
        self.convert_button.clicked.connect(self.convert_to_speech)
        layout.addWidget(self.convert_button)

        central_widget.setLayout(layout)

    def load_file(self):
        """Load text from a file into the text input."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_input.setText(file.read())
            except Exception as e:
                self.label.setText(f"Error: {e}")

    def save_file_dialog(self):
        """Open a file dialog to select where to save the output audio."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Audio File", "", "WAV Files (*.wav)")
        if file_path:
            self.output_audio_path = file_path
            self.label.setText(f"Output file set to: {file_path}")

    def convert_to_speech(self):
        """Convert text to speech."""
        text_to_speak = self.text_input.text().strip()
        if not text_to_speak:
            self.label.setText("Please provide text to convert.")
            return

        if not self.output_audio_path:
            self.label.setText("Please select an output file location.")
            return

        model_name = self.voice_selector.currentText()

        try:
            self.tts_backend.generate_audio(text_to_speak, self.output_audio_path, model_name)
            self.label.setText(f"TTS finished! Saved to {self.output_audio_path}")
        except Exception as e:
            self.label.setText(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = TTSApp()
    window.show()
    app.exec_()
