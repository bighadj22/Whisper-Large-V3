# Whisper-Large-V3
Audio Transcription with Whisper Large V3
Audio Transcription with Whisper Large V3
This repository contains a Python script for transcribing audio files using the whisper-large-v3 model via the Replicate API.

Overview
The script processes audio files (.mp3 or .wav) from a specified directory, utilizing the whisper-large-v3 model for transcription. Users are prompted to decide whether to continue with the next file after each transcription.

Requirements
Python 3
replicate Python package
python-dotenv package for environment variable management
Setup
Clone this repository.

Install required packages:

bash
Copy code
pip install replicate python-dotenv
Create a .env file in the project root and add your Replicate API token:

env
Copy code
REPLICATE_API_TOKEN=your_api_token_here
Usage
Run the script using Python:

bash
Copy code
python transcribe_audio.py
The script will process each audio file in the specified directory and output the transcription.
