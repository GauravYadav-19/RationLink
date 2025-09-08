import pandas as pd
import random

def generate_dataset(n=200):
    data = []
    for i in range(n):
        BeneficiaryID = f"B{1000+i}"
        FamilySize = random.randint(1, 8)
        MonthlyLimit = FamilySize * 5
        Date = pd.date_range("2025-09-01", "2025-09-30").to_series().sample().iloc[0].date()
        ShopID = f"S{random.randint(1, 10)}"
        fraud = random.choices([0, 1], weights=[85, 15])[0]
        if fraud == 0:
            Claimed = random.randint(int(MonthlyLimit*0.7), MonthlyLimit)
        else:
            Claimed = random.randint(MonthlyLimit+1, MonthlyLimit+10)
        data.append([BeneficiaryID, FamilySize, MonthlyLimit, Claimed, Date, ShopID, fraud])
    
    df = pd.DataFrame(data, columns=["BeneficiaryID","FamilySize","MonthlyLimit","Claimed","Date","ShopID","FraudFlag"])
    df.to_csv("../dataset/ration_dummy_dataset.csv", index=False)
    return df

def detect_fraud(df):
    df['DetectedFraud'] = df.apply(lambda row: 1 if row['Claimed'] > row['MonthlyLimit'] else 0, axis=1)
    return df

# For testing locally
if __name__ == "__main__":
    df = generate_dataset()
    df = detect_fraud(df)
    print(df.head())