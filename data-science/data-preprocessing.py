import pandas as pd
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv("data/raw_data.csv")

# Handle missing values
imputer = SimpleImputer(strategy="mean")
df["age"] = imputer.fit_transform(df[["age"]])

# Encode categorical variables
df = pd.get_dummies(df, columns=["gender", "occupation"])

# Scale numerical features
df["income"] = (df["income"] - df["income"].mean()) / df["income"].std()

# Save processed data
df.to_csv("data/processed_data.csv", index=False)
print("Data preprocessing completed!")
