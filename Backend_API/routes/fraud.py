from flask import Blueprint, jsonify, request
from models.transaction import db, Transaction
from fraud_detection import detect_fraud
import pandas as pd

fraud_bp = Blueprint("fraud", __name__)

@fraud_bp.route("/detect-fraud", methods=["POST"])
def detect_fraud_api():
    data = request.json
    df = pd.DataFrame([data])
    result = detect_fraud(df)
    return jsonify(result.to_dict(orient="records"))

@fraud_bp.route("/fraud-stats", methods=["GET"])
def fraud_stats():
    total = Transaction.query.count()
    frauds = Transaction.query.filter_by(FraudFlag=1).count()
    return jsonify({
        "total": total,
        "frauds": frauds,
        "fraud_percentage": round((frauds/total)*100, 2) if total > 0 else 0
    })