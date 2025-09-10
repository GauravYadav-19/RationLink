from flask import Flask, jsonify
from flask_cors import CORS
from models.transaction import db
from routes.dataset import dataset_bp
from routes.fraud import fraud_bp
import os

app = Flask(__name__)
CORS(app)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///rationlink.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register Blueprints
app.register_blueprint(dataset_bp, url_prefix="/api")
app.register_blueprint(fraud_bp, url_prefix="/api")

@app.route("/api/health")
def health_check():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)