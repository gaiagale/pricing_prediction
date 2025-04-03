from src import config
import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
import pickle
import logging

def load_data():
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT * FROM {config.RAW_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

#we can use raw data because there's nothing to preprocess

def train_model():
    df = load_data()
    #split data in train and test
    X = df[['X1 transaction date', 'X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores', 'X5 latitude', 'X6 longitude']]  # Seleziona più colonne per le variabili indipendenti
    y = df['Y house price of unit area']
    X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(X, y, df.index, test_size=0.2, random_state=42)

    #train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    #predict model
    y_pred = model.predict(X_test)

    #save model
    logging.info('Saving model...')
    with open(os.path.join(config.MODELS_PATH, "linear_regression.pickle"), "wb") as file: 
           pickle.dump(model, file) 

    
    # Create a DataFrame for the test set with predictions
    test_df = df.loc[test_idx].copy()  # Copy test set rows
    test_df['prediction'] = y_pred  # Add predictions


    # Compute metrics
    metrics = {
        'mse': mean_squared_error(y_test, y_pred),
        'r2': r2_score(y_test, y_pred)
    }

    # Connect to the database
    conn = sqlite3.connect(config.DATABASE_PATH)

    # saving predictions
    test_df.to_sql(config.PREDICTIONS_TABLE, conn, if_exists='replace', index=False)
    
    # saving results
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_sql(config.EVALUATION_TABLE, conn,
                      if_exists='replace', index=False)
    # Commit and close the connection
    conn.commit()
    conn.close()