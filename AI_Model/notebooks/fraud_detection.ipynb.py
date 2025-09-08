#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import random

# Number of rows
n = 200  

data = []
for i in range(n):
    BeneficiaryID = f"B{1000+i}"          # Unique ID
    FamilySize = random.randint(1, 8)     # 1–8 members
    MonthlyLimit = FamilySize * 5         # 5 kg per person
    Date = pd.date_range("2025-09-01", "2025-09-30").to_series().sample().iloc[0].date()
    ShopID = f"S{random.randint(1, 10)}"  # 10 shops

    # Fraud or legit?
    fraud = random.choices([0, 1], weights=[85, 15])[0]  # 15% fraud
    if fraud == 0:
        Claimed = random.randint(int(MonthlyLimit*0.7), MonthlyLimit)
    else:
        Claimed = random.randint(MonthlyLimit+1, MonthlyLimit+10)  # Over limit fraud

    data.append([BeneficiaryID, FamilySize, MonthlyLimit, Claimed, Date, ShopID, fraud])

# Create DataFrame
df = pd.DataFrame(data, columns=["BeneficiaryID", "FamilySize", "MonthlyLimit", "Claimed", "Date", "ShopID", "FraudFlag"])

# Save to dataset folder
df.to_csv("../dataset/ration_dummy_dataset.csv", index=False)

df.head()


# In[3]:


df['DetectedFraud'] = df.apply(lambda row: 1 if row['Claimed'] > row['MonthlyLimit'] else 0, axis=1)
print("Detection Accuracy:", (df['FraudFlag'] == df['DetectedFraud']).mean())
df[df['DetectedFraud'] == 1].head()


# In[ ]:




