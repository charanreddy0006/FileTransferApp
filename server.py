import os
from flask import Flask, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "received_files")

@app.route('/upload', methods=['POST'])
def upload_file():
    print("Incoming request...")

    if 'file' not in request.files:
        print("No file part")
        return "No file", 400

    file = request.files['file']

    if file.filename == '':
        print("No selected file")
        return "No selected file", 400
    from werkzeug.utils import secure_filename

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    print("Saved at:", filepath)

    return "File uploaded successfully", 200


if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)