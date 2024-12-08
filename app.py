import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
from gtts import gTTS
import tempfile

app = Flask(__name__)
CORS(app)

# Make sure the GEMINI_API_KEY is set in the environment
genai.configure(api_key=os.environ.get(""))

# Initialize the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Specify the correct model name
    generation_config=generation_config,
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        
        # Start a chat session with Gemini model
        chat_session = model.start_chat(history=[])
        gemini_response = chat_session.send_message(user_message)

        response = gemini_response.text if gemini_response else "I'm sorry, I couldn't understand that. Can you please rephrase your question?"

        # Check if the user wants voice output
        voice_enabled = request.json.get("voice_enabled", False)

        if voice_enabled:
            # Generate speech from the response using gTTS
            tts = gTTS(text=response, lang='en')
            # Save the speech to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
            tts.save(temp_file.name)
            return jsonify({"response": response, "audio_file": temp_file.name})

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": "An error occurred: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
