import os
import sys
sys.path.append(os.path.abspath('..'))
from src import config
import streamlit as st
import pickle
import numpy as np

# Load the model 
with open(f"{config.MODELS_PATH}linear_regression.pickle", "rb") as file:
    lin_reg = pickle.load(file)

# Load the stats: and use them to impute missing in UI
with open(f"{config.DATAFRAME_PATH}df_stats.pickle", "rb") as file:
    stats = pickle.load(file)


x5_min, x5_max, x6_min, x6_max = stats.iloc[1,4], stats.iloc[2,4], stats.iloc[1,5], stats.iloc[2,5]
X = stats.iloc[0, :-1].to_frame().transpose()


st.title("Real Estate Pricing Prediction")

# Text input
options = ["Latitude and Longitude", "House Age, Distance from nearest MRT, Number of convenience stores", "All of them"]
choice = st.selectbox("Which inputs would you like to use for your prediction?", options)


if st.button("Next"):
    if choice == options[0]:
        user_latitude = st.number_input("Insert latitude", min_value = x5_min, max_value = x5_max, value = X['X5 latitude'].iloc[0])
        user_longitude = st.number_input("Insert longitude", min_value = x6_min, max_value = x6_max, value = X['X6 longitude'].iloc[0])
        
        if st.button('Predict'):
            list = [X['X1 transaction date'].iloc[0], X['X2 house age'].iloc[0], X['X3 distance to the nearest MRT station'].iloc[0], X['X4 number of convenience stores'].iloc[0], user_latitude, user_longitude]
            prediction = lin_reg.predict(list)
            st.success(f"Your house price of unit area is: {prediction}")

    elif choice == options[1]:
        user_house_age = st.number_input("Insert house age", min_value = np.float64(0), max_value = np.float64(50), value = X['X2 house age'].iloc[0])
        user_MRT = st.number_input("Insert distance from nearest MRT", min_value = np.float64(0), max_value = np.float64(7000), value = X['X3 distance to the nearest MRT station'].iloc[0])
        user_convenience_stores = st.number_input("Insert number of convenience stores", min_value = np.float64(0), max_value = np.float64(10), value = X['X4 number of convenience stores'].iloc[0])
        
        if st.button('Predict'):
            list = [X['X1 transaction date'].iloc[0], user_house_age, user_MRT, user_convenience_stores, X['X5 latitude'].iloc[0], X['X6 longitude'].iloc[0]]
            prediction = lin_reg.predict(list)
            st.success(f"Your house price of unit area is: {prediction}")

    else:
        user_latitude = st.number_input("Insert latitude", min_value = x5_min, max_value = x5_max, value = X['X5 latitude'].iloc[0])
        user_longitude = st.number_input("Insert longitude", min_value = x6_min, max_value = x6_max, value = X['X6 longitude'].iloc[0])
        user_house_age = st.number_input("Insert house age", min_value = np.float64(0), max_value = np.float64(50), value = X['X2 house age'].iloc[0])
        user_MRT = st.number_input("Insert distance from nearest MRT", min_value = np.float64(0), max_value = np.float64(7000), value = X['X3 distance to the nearest MRT station'].iloc[0])
        user_convenience_stores = st.number_input("Insert number of convenience stores", min_value = np.float64(0), max_value = np.float64(10), value = X['X4 number of convenience stores'].iloc[0])
        
        if st.button('Predict'):
            list = [X['X1 transaction date'].iloc[0], user_house_age, user_MRT, user_convenience_stores, user_latitude, user_longitude]
            prediction = lin_reg.predict(list)
            st.success(f"Your house price of unit area is: {prediction}")
