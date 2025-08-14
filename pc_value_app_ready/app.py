import pandas as pd
import streamlit as st
import os

# ======== Load CPU Data ========
if os.path.exists("cpus.csv"):
    cpus = pd.read_csv("cpus.csv")
else:
    cpus = pd.DataFrame([
        {"name": "Intel Core i5-12400F", "score": 14500},
        {"name": "Intel Core i7-12700K", "score": 20000},
        {"name": "Intel Core i9-13900K", "score": 35000},
        {"name": "AMD Ryzen 5 5600X", "score": 15500},
        {"name": "AMD Ryzen 7 5800X3D", "score": 28000},
        {"name": "AMD Ryzen 9 7950X", "score": 42000},
    ])

# ======== Load GPU Data ========
if os.path.exists("gpus.csv"):
    gpus = pd.read_csv("gpus.csv")
else:
    gpus = pd.DataFrame([
        {"name": "NVIDIA RTX 4090", "score": 50000},
        {"name": "NVIDIA RTX 4080", "score": 42000},
        {"name": "NVIDIA RTX 4070 Ti", "score": 35000},
        {"name": "NVIDIA RTX 4060 Ti", "score": 22000},
        {"name": "NVIDIA RTX 3060 Ti", "score": 18000},
        {"name": "AMD RX 7900 XTX", "score": 45000},
        {"name": "AMD RX 7800 XT", "score": 34000},
        {"name": "AMD RX 6700 XT", "score": 20000},
    ])

# ======== Streamlit UI ========
st.title("PC Value Checker")

cpu_choice = st.selectbox("Choose CPU", cpus["name"])
gpu_choice = st.selectbox("Choose GPU", gpus["name"])

# ======== Get Scores Safely ========
def safe_get_score(df, part_name):
    row = df.loc[df["name"] == part_name, "score"]
    if not row.empty:
        return row.iloc[0]
    else:
        return None

cpu_score = safe_get_score(cpus, cpu_choice)
gpu_score = safe_get_score(gpus, gpu_choice)

if cpu_score is None or gpu_score is None:
    st.error("Could not find benchmark score for the selected part.")
else:
    total_score = cpu_score + gpu_score
    st.write(f"CPU Score: {cpu_score}")
    st.write(f"GPU Score: {gpu_score}")
    st.write(f"Total Performance Score: {total_score}")
