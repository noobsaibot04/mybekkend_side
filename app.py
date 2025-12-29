from flask import Flask, send_from_directory
from flask_cors import CORS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(BASE_DIR, "pdfs")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Tabiiy fanlar backend ishlayapti ✅"

@app.route("/pdfs/<path:filename>")
def serve_pdf(filename):
    return send_from_directory(PDF_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
