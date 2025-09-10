from flask import Blueprint, jsonify, request
from models.transaction import db, Transaction
from fraud_detection import generate_dataset

dataset_bp = Blueprint("dataset", __name__)

@dataset_bp.route("/generate-dataset", methods=["POST"])
def generate_dataset_api():
    n = request.json.get("n", 100)
    df = generate_dataset(n=n)
    
    # Save to DB
    for _, row in df.iterrows():
        txn = Transaction(
            BeneficiaryID=row["BeneficiaryID"],
            FamilySize=row["FamilySize"],
            MonthlyLimit=row["MonthlyLimit"],
            Claimed=row["Claimed"],
            Date=row["Date"],
            ShopID=row["ShopID"],
            FraudFlag=row["FraudFlag"],
        )
        db.session.add(txn)
    db.session.commit()
    
    return jsonify({"message": f"{n} records generated and saved"}), 201

@dataset_bp.route("/transactions", methods=["GET"])
def get_transactions():
    limit = int(request.args.get("limit", 10))
    txns = Transaction.query.limit(limit).all()
    return jsonify([{
        "id": t.id,
        "BeneficiaryID": t.BeneficiaryID,
        "FamilySize": t.FamilySize,
        "MonthlyLimit": t.MonthlyLimit,
        "Claimed": t.Claimed,
        "Date": t.Date,
        "ShopID": t.ShopID,
        "FraudFlag": t.FraudFlag,
    } for t in txns])