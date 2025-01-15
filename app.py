from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
from dotenv import load_dotenv
import os
from bot import FinanceChatbotModel
from tts_demo import text_to_speech

# Initialize Flask app
app = Flask(__name__, template_folder=r"E:\K M Archana\Project\Cold-Call-AI\templates")
CORS(app)

# Load environment variables
load_dotenv()

# Access API keys
api_key = os.getenv("GEMINI_API_KEY")
tts_api_key = os.getenv("TTS_API_KEY")

# Initialize the chatbot model
chatbot = FinanceChatbotModel(api_key)

# Path to store generated audio files
AUDIO_DIRECTORY = r"E:\K M Archana\Project\Cold-Call-AI\Documents"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chatbot", methods=["POST"])
def chatbot_interaction():
    data = request.get_json()  # Parse JSON from request
    user_message = data.get("message", "")  # Get the user's message

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Generate chatbot response
    bot_response = chatbot.get_response(user_message)

    # Generate audio file from response
    output_file = os.path.join(AUDIO_DIRECTORY, "output_audio.wav")
    text_to_speech(tts_api_key, bot_response, output_file)

    # Return the URL for the audio file
    return jsonify({"audio_url": f"http://127.0.0.1:5000/audio/output_audio.wav"})

@app.route("/audio/<filename>")
def serve_audio(filename):
    file_path = os.path.join(AUDIO_DIRECTORY, filename)
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='audio/wav')
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
