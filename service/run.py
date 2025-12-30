import os
import logging
from flask import Flask

from app.routes.pdf import pdf_bp

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.register_blueprint(pdf_bp)

@app.route("/")
def index():
    return "Geräteausleihe Microservice is running"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    debug = os.environ.get("FLASK_DEBUG", "").lower() in ("1", "true", "yes")
    app.run(host="0.0.0.0", port=port, debug=debug)
