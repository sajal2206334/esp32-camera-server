from flask import Flask, request, send_from_directory, render_template
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, 'latest.jpg')
        file.save(filepath)
        return 'Image uploaded', 200
    return 'No image received', 400

@app.route('/')
def index():
    timestamp = int(datetime.now().timestamp())
    return render_template('index.html', timestamp=timestamp)

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)