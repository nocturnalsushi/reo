import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import markdown2

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def generate_response(user_message, history):
    messages = [
        {
            "role": "system",
            "content": "You're Rio, a multilingual chatbot that assess the user's language and asks if your understanding is correct. Following which you you speak in their initial language and give a fun fact regarding their chosen one and ask if the user would like to learn the language interactively with you. Please be a teacher from then onwards and encourage the user to ask pronunciations, spellings et cetera."
        }
    ]
    messages.extend(history)
    messages.append({
        "role": "user",
        "content": user_message
    })
    
    data = {
        "model": "llama3-8b-8192",
        "messages": messages,
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    history = request.json.get('history', [])
    response = generate_response(user_message, history)
    
    try:
        assistant_message = response['choices'][0]['message']['content']
        # Convert markdown to HTML
        assistant_message_html = markdown2.markdown(assistant_message)
        return jsonify({'message': assistant_message_html})
    except (KeyError, IndexError):
        return jsonify({'error': 'Unable to fetch response from Groq API.', 'details': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
