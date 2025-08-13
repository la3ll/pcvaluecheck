import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# --- Paths ---
BASE_DIR = os.path.join(os.path.dirname(__file__), "data")
CPUS_CSV = os.path.join(BASE_DIR, "cpus.csv")
GPUS_CSV = os.path.join(BASE_DIR, "gpus.csv")
PARTS_CSV = os.path.join(BASE_DIR, "parts_meta.csv")

# --- Load data ---
cpus = pd.read_csv(CPUS_CSV)
gpus = pd.read_csv(GPUS_CSV)
parts_meta = pd.read_csv(PARTS_CSV)

# --- Streamlit App ---
st.title("PC Value Checker")

st.write("This app helps you evaluate PC builds, estimate gaming performance, and score value.")

# Example: Select CPU
cpu_choice = st.selectbox("Select CPU", cpus["name"].tolist())
gpu_choice = st.selectbox("Select GPU", gpus["name"].tolist())

cpu_score = cpus.loc[cpus["name"] == cpu_choice, "score"].values[0]
gpu_score = gpus.loc[gpus["name"] == gpu_choice, "score"].values[0]

st.write(f"CPU Score: {cpu_score}")
st.write(f"GPU Score: {gpu_score}")

# Example value score calculation
total_score = cpu_score + gpu_score
price = cpus.loc[cpus["name"] == cpu_choice, "price"].values[0] + gpus.loc[gpus["name"] == gpu_choice, "price"].values[0]
value_score = min(int(total_score / price * 1000), 100)

st.write(f"Estimated Value Score: {value_score}/100")

# Optional: Plot scores
fig, ax = plt.subplots()
ax.bar(["CPU", "GPU"], [cpu_score, gpu_score])
ax.set_ylabel("Performance Score")
st.pyplot(fig)
