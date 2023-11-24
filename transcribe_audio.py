import os
import replicate
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Set up the Replicate client with the API token from the environment
client = replicate.Client()

# Path to the folder containing audio files
audio_folder_path = './audio'

# Function to transcribe an audio file
def transcribe_audio(file_path):
    # Running the whisper-large-v3 model on the audio file
    output = client.run(
        "nateraw/whisper-large-v3:e13f98aa561f28e01abc92a01a4d48d792bea2d8d1a4f9e858098d794f4fe63f",
        input={"filepath": open(file_path, "rb")}
    )
    return output

# Function to ask the user whether to continue to the next file
def ask_continue():
    while True:
        answer = input("Do you want to process the next audio file? (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        else:
            print("Please answer 'yes' or 'no'.")

# Main function to process audio files in the folder
def process_audio_files(folder_path):
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing {filename}...")
            
            # Transcribing the audio file
            transcription = transcribe_audio(file_path)
            print(f"Transcription for {filename}: {transcription}")

            # Asking the user if they want to continue to the next file
            if not ask_continue():
                break

# Execute the main function
if __name__ == "__main__":
    process_audio_files(audio_folder_path)
