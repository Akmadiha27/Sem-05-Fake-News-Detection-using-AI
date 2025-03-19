from flask import Flask, request, jsonify, send_from_directory
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

app = Flask(__name__)

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("my_awesome_model")
model = AutoModelForSequenceClassification.from_pretrained("my_awesome_model")

# Serve the main HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static files (CSS, JavaScript, images)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')

    # Tokenize and predict
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    prediction = logits.argmax().item()
    
    # Assuming label 0 = "fake" and label 1 = "real"
    label = "fake" if prediction == 0 else "real"
    
    return jsonify({"prediction": label})

if __name__ == '__main__':
    app.run(debug=True)
