import pandas as pd
import random

def generate_dataset(n=100):
    data = []
    for i in range(n):
        FamilySize = random.randint(1, 6)
        MonthlyLimit = FamilySize * 5
        Claimed = random.randint(1, MonthlyLimit + 3)
        fraud = 1 if Claimed > MonthlyLimit else 0
        data.append({
            "BeneficiaryID": f"B{i+1}",
            "FamilySize": FamilySize,
            "MonthlyLimit": MonthlyLimit,
            "Claimed": Claimed,
            "Date": "2025-09-11",
            "ShopID": f"S{random.randint(1, 5)}",
            "FraudFlag": fraud,
        })
    return pd.DataFrame(data)

def detect_fraud(df):
    df["DetectedFraud"] = (df["Claimed"] > df["MonthlyLimit"]).astype(int)
    return df