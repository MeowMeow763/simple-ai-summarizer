from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline("summarization")

@app.route('/')
def home():
    return "Simple AI Summarizer is running!"

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return jsonify({"summary": summary})

# Required for deployment on Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
