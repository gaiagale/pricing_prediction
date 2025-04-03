import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for raw data (Excel files)
RAW_DATA_PATH = os.path.join(BASE_DIR, "../data/raw/")

# SQLite Database Path
DATABASE_PATH = os.path.join(BASE_DIR, "../database/pricing.db")

# Raw Data Table Name
RAW_TABLE = "raw_prices"

# Saved models
MODELS_PATH = "../models/"

# Saved stats
DATAFRAME_PATH = "../data/"

# Predictions Table Name
PREDICTIONS_TABLE = "predictions"

# model evaluation
EVALUATION_TABLE = "metrics_results"

# Logging Configuration
LOGGING_LEVEL = "INFO"