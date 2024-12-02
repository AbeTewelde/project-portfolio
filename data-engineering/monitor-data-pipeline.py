import logging
import time

# Configure logging
logging.basicConfig(filename="pipeline.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Example pipeline functions
def extract():
    logging.info("Extraction started")
    time.sleep(1)  # Simulate work
    logging.info("Extraction completed")
    return {"data": [1, 2, 3]}

def transform(data):
    logging.info("Transformation started")
    time.sleep(1)  # Simulate work
    transformed_data = [x * 2 for x in data]
    logging.info("Transformation completed")
    return transformed_data

def load(data):
    logging.info("Loading started")
    time.sleep(1)  # Simulate work
    logging.info(f"Data loaded: {data}")
    logging.info("Loading completed")

# Run pipeline
if __name__ == "__main__":
    logging.info("Pipeline execution started")
    try:
        raw_data = extract()
        transformed_data = transform(raw_data["data"])
        load(transformed_data)
        logging.info("Pipeline execution completed successfully")
    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}")
