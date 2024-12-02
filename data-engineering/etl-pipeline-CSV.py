import pandas as pd
import os
from sqlalchemy import create_engine

# Configuration
input_folder = "data/input/"
output_folder = "data/output/"
database_url = "sqlite:///etl_database.db"  # Replace with your database URL

# Extract: Load CSV files
def extract_data(folder):
    all_dataframes = []
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder, file))
            all_dataframes.append(df)
    return pd.concat(all_dataframes, ignore_index=True)

# Transform: Clean and process data
def transform_data(df):
    df.dropna(inplace=True)  # Remove missing values
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]  # Standardize column names
    return df

# Load: Save data to database
def load_data(df, table_name, db_url):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists="replace", index=False)

# Run ETL process
if __name__ == "__main__":
    raw_data = extract_data(input_folder)
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data, "processed_data", database_url)
    print("ETL process completed!")
