import pandas as pd

# Configuration
input_file = "data/large_dataset.csv"
output_folder = "data/partitions/"
partition_size = 10000  # Number of rows per partition

# Partitioning function
def partition_data(input_file, output_folder, size):
    df = pd.read_csv(input_file, chunksize=size)
    for i, chunk in enumerate(df):
        chunk.to_csv(f"{output_folder}partition_{i + 1}.csv", index=False)
        print(f"Partition {i + 1} saved.")

# Run partitioning
if __name__ == "__main__":
    partition_data(input_file, output_folder, partition_size)
