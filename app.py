from flask import Flask, render_template, request, send_file
from transformers import AutoProcessor, AutoModel
import torch
from PIL import Image
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apply-filter', methods=['POST'])
def filter_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    file = request.files['image']
    if file:
        # Save uploaded image
        input_path = os.path.join(UPLOAD_FOLDER, 'input.jpg')
        file.save(input_path)
        
        # Process image (placeholder for now)
        # Add your AI processing here
        
        return send_file(input_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)