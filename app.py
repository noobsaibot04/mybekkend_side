from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

# -------------------------
# Asosiy sozlamalar
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(BASE_DIR, "pdfs")

app = Flask(__name__)
CORS(app)  # Netlify frontend bilan ishlashi uchun

# -------------------------
# Asosiy test route
# -------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Tabiiy fanlar backend ishlayapti ✅"
    })

# -------------------------
# PDF fayllarni berish
# -------------------------
@app.route("/pdfs/<path:filename>")
def serve_pdf(filename):
    return send_from_directory(PDF_FOLDER, filename, as_attachment=False)

# -------------------------
# Serverni ishga tushirish (Render uchun mos)
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

