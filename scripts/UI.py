import os
import sys
sys.path.append(os.path.abspath('..'))
from src import config
import streamlit as st
import pickle
import sqlite3
import pandas as pd

# Load the model 
with open(f"{config.MODELS_PATH}linear_regression.pickle", "rb") as file:
    lin_reg = pickle.load(file)

def load_data():
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT * FROM {config.RAW_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


st.title("Real Estate Pricing Prediction")

# Text input
options = ["Latitude and Longitude", "House Age, Distance from nearest MRT, Number of convenience stores"]
choice = st.selectbox("Which inputs would you like to use for your prediction?", options)