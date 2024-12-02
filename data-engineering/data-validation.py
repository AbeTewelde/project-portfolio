import pandas as pd

# Validation functions
def validate_completeness(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    return True

def validate_data_types(df, column_types):
    for column, dtype in column_types.items():
        if column in df.columns and not df[column].dtype == dtype:
            raise TypeError(f"Column {column} has incorrect type. Expected {dtype}, found {df[column].dtype}.")
    return True

# Example usage
if __name__ == "__main__":
    df = pd.read_csv("data/input/sample.csv")
    required_columns = ["id", "name", "age"]
    column_types = {"id": "int64", "age": "float64"}

    try:
        validate_completeness(df, required_columns)
        validate_data_types(df, column_types)
        print("Data validation passed!")
    except (ValueError, TypeError) as e:
        print(f"Data validation failed: {e}")
