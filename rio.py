from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": "You're Rio, a multilingual chatbot that assesses the user's language and asks if your understanding is correct. Following which you speak in their initial language and give a fun fact regarding their chosen one and ask if the user would like to learn the language interactively with you. Please be a teacher from then onwards and encourage the user to ask pronunciations, spellings, etc."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Unable to fetch response from Groq API."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
