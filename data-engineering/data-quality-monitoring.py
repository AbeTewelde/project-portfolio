import pandas as pd

# Load dataset
df = pd.read_csv("data/processed_data.csv")

# Data quality checks
def calculate_data_quality(df):
    completeness = df.notnull().mean().mean() * 100
    duplicates = df.duplicated().sum()
    return {
        "Completeness (%)": completeness,
        "Duplicate Rows": duplicates,
    }

# Example usage
if __name__ == "__main__":
    metrics = calculate_data_quality(df)
    print("Data Quality Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")
