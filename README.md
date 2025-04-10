# Zero-Shot Multilingual Text-to-Speech Model

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![TTS Version](https://img.shields.io/badge/TTS-0.22.0-green.svg)](https://github.com/coqui-ai/TTS)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A versatile zero-shot multilingual text-to-speech model that converts text, images with text (OCR), and audio transcriptions into synthesized speech in multiple languages with both male and female voice options.

![Model Overview](https://drive.google.com/uc?export=view&id=YOUR_IMAGE_ID_HERE)

## ✨ Features

- **Multi-Modal Input**: Accept text, images (OCR), or audio (speech-to-text) as input
- **Zero-Shot Voice Synthesis**: Generate speech without pre-training on specific voices
- **Multiple Languages**: Support for 20 languages including English, Hindi, Marathi, Bengali, French, German, Spanish, and more
- **Gender Selection**: Choose between male and female voice options
- **User-Friendly Interface**: Easy-to-use Gradio web interface
- **Error Handling**: Robust error handling and fallback mechanisms

## 🚀 Quick Start

### Prerequisites

```bash
# Install required libraries
pip install torch torchaudio torchvision
pip install numpy==1.26.4 pandas==1.5.3 networkx==2.8.8
pip install matplotlib seaborn opencv-python pytesseract
pip install tts==0.22.0 gtts gradio
pip install SpeechRecognition pydub librosa soundfile
```

### Setup Voice References

```python
import os
import librosa
import soundfile as sf

# Create a folder for voice references
voice_ref_path = "/content/drive/MyDrive/voice_references"
os.makedirs(voice_ref_path, exist_ok=True)

# Define source MP3 files from your dataset
voice_sources = {
    "male": [
        "/path/to/male_voice1.mp3",
        "/path/to/male_voice2.mp3",
        "/path/to/male_voice3.mp3"
    ],
    "female": [
        "/path/to/female_voice1.mp3",
        "/path/to/female_voice2.mp3",
        "/path/to/female_voice3.mp3"
    ]
}

# Convert all references
for gender, sources in voice_sources.items():
    for i, source_path in enumerate(sources, 1):
        suffix = "" if i == 1 else str(i)
        output_path = os.path.join(voice_ref_path, f"{gender}_reference{suffix}.wav")
        
        y, sr = librosa.load(source_path, sr=None)
        sf.write(output_path, y, sr)
```

### Run the Model

```bash
python zero_shot_tts_model.py
```

## 📚 Supported Languages

| Language | Code | Language | Code |
|----------|------|----------|------|
| English | en | Japanese | ja |
| Hindi | hi | Russian | ru |
| Marathi | mr | Portuguese | pt |
| Bengali | bn | Italian | it |
| French | fr | Turkish | tr |
| German | de | Dutch | nl |
| Spanish | es | Swedish | sv |
| Chinese | zh-cn | Greek | el |
| Arabic | ar | Polish | pl |
| Korean | ko | Tamil | ta |

## 🔍 Model Architecture

This model uses the XTTS v2 architecture from Coqui TTS to perform zero-shot text-to-speech synthesis. It takes advantage of pre-trained multilingual models and incorporates:

1. **Input Processing Module**: Handles text, image, and audio inputs
2. **Language Processing**: Maps languages to appropriate codes for different libraries
3. **Voice Reference System**: Uses sample audio to clone voice characteristics
4. **Speech Synthesis**: Generates speech in the target language with the selected voice

## 📊 Sample Datasets

For testing the image and audio processing capabilities, create sample datasets:

```
/content/sample_datasets/
├── images/         # Add 1-2 images with clear text
├── audio/          # Add 1-2 audio files with clear speech
└── README.txt      # Contains dataset guidelines
```

## 🛠️ Troubleshooting

If you encounter issues:

1. **TTS Model Loading**: Ensure you have enough memory and the correct TTS version
2. **Voice Reference Issues**: Verify that voice reference files exist and contain clear speech
3. **Language Support**: Check if the selected language is properly supported by the model
4. **OCR Problems**: Ensure images have clear, high-contrast text
5. **Speech Recognition**: Verify audio files have clear speech with minimal background noise

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Coqui TTS](https://github.com/coqui-ai/TTS) for the XTTS model
- [Gradio](https://gradio.app/) for the web interface
- [PyTesseract](https://github.com/madmaze/pytesseract) for OCR capabilities
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) for audio transcription
