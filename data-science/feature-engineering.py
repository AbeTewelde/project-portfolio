import pandas as pd

# Load dataset
df = pd.read_csv("data/processed_data.csv")

# Feature creation
df["age_income_ratio"] = df["age"] / df["income"]
df["is_high_income"] = df["income"].apply(lambda x: 1 if x > df["income"].mean() else 0)

# Save the dataset with new features
df.to_csv("data/feature_engineered_data.csv", index=False)
print("Feature engineering completed!")
