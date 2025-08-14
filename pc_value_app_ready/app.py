import pandas as pd
import streamlit as st

# Try loading CSV, else use fallback
try:
    cpus = pd.read_csv("cpus.csv")
except FileNotFoundError:
    cpus = pd.DataFrame([
        {"name": "Intel Core i5-12400F", "score": 14500},
        {"name": "Intel Core i7-12700K", "score": 20000},
        {"name": "AMD Ryzen 5 5600X", "score": 15500},
    ])

try:
    gpus = pd.read_csv("gpus.csv")
except FileNotFoundError:
    gpus = pd.DataFrame([
        {"name": "NVIDIA RTX 3060 Ti", "score": 18000},
        {"name": "NVIDIA RTX 3080", "score": 25000},
        {"name": "AMD RX 6700 XT", "score": 20000},
    ])

# Streamlit UI
cpu_choice = st.selectbox("Choose CPU", cpus["name"])
gpu_choice = st.selectbox("Choose GPU", gpus["name"])

# Safely get scores
cpu_score = cpus.loc[cpus["name"] == cpu_choice, "score"].iloc[0]
gpu_score = gpus.loc[gpus["name"] == gpu_choice, "score"].iloc[0]

st.write(f"CPU Score: {cpu_score}")
st.write(f"GPU Score: {gpu_score}")
