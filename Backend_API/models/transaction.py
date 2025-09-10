from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    BeneficiaryID = db.Column(db.String(50), nullable=False)
    FamilySize = db.Column(db.Integer, nullable=False)
    MonthlyLimit = db.Column(db.Integer, nullable=False)
    Claimed = db.Column(db.Integer, nullable=False)
    Date = db.Column(db.String(20), nullable=False)
    ShopID = db.Column(db.String(50), nullable=False)
    FraudFlag = db.Column(db.Integer, nullable=False, default=0)