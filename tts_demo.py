import requests
import os
from pydub import AudioSegment
from playsound import playsound

# Ensure custom temporary directory is set up at the start
custom_temp_dir = r"E:\K M Archana\Project\Cold-Call-AI\MyTemp"
if not os.path.exists(custom_temp_dir):
    os.makedirs(custom_temp_dir)

# Change the environment variable for TEMP and TMP
os.environ["TEMP"] = custom_temp_dir
os.environ["TMP"] = custom_temp_dir

def text_to_speech(api_key, text, output_file=None):
    # Set ffmpeg and ffplay paths explicitly
    AudioSegment.converter = r"E:\K M Archana\Project\Cold-Call-AI\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"
    AudioSegment.ffmpeg = r"E:\K M Archana\Project\Cold-Call-AI\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"
    AudioSegment.ffplay = r"E:\K M Archana\Project\Cold-Call-AI\ffmpeg-7.1-essentials_build\bin\ffplay.exe"
  
    # Verify if paths are correctly set
    print("FFmpeg Path:", AudioSegment.ffmpeg)
    print("FFplay Path:", AudioSegment.ffplay)

    # Corrected URL with model
    url = "https://waves-api.smallest.ai/api/v1/Lightning/get_speech"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_id": "james",  # Replace with the voice you'd like to use
        "speed": 1,
        "sample_rate": 24000,
        "add_wav_header": True
    }

    try:
        # Save the audio file (as WAV) in the Documents folder
        if output_file is None:
            output_file = r"E:\K M Archana\Project\Cold-Call-AI\Documents\output_audio.wav"
        
        # Send POST request to TTS API
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise error for failed requests

        # Save the audio file locally
        with open(output_file, "wb") as audio_file:
            audio_file.write(response.content)

        print(f"Audio saved to {output_file}")

        # Play the audio using playsound
        #playsound(output_file)

    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
    except Exception as e:
        print(f"Error playing audio: {e}")

if __name__ == "__main__":
    # Replace with your Smallest.ai API key
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2NzgyN2M2ZTQzNjMwNGZhZDUwNmY5MGQiLCJrZXlOYW1lIjoidGV4dC10by1zcGVlY2giLCJpYXQiOjE3MzY2MTQ4MjJ9.s_C7MGwkgYVYOseO2EU3eCPpl7rIK6cIwdAjwvybhyo"  # Insert your API key here

    # Text to be converted to speech
    text = "Hello , this is a demo of the text-to-speech feature using the Smallest.ai API."

    # Call the TTS function
    text_to_speech(api_key, text)
