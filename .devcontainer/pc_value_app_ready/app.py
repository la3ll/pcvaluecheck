
import streamlit as st
import pandas as pd

RAW_BASE = "https://raw.githubusercontent.com/la3ll/pcvaluecheck/main/pc_value_app/data/"

st.title("💻 PC Value Checker")
st.write("Compare PC build performance, see which games it can run, and find value scores.")

# Load CSVs from GitHub
cpus = pd.read_csv(RAW_BASE + "cpus.csv")
gpus = pd.read_csv(RAW_BASE + "gpus.csv")
parts_meta = pd.read_csv(RAW_BASE + "parts_meta.csv")

st.header("Available CPUs")
st.dataframe(cpus)

st.header("Available GPUs")
st.dataframe(gpus)

st.header("Other Parts")
st.dataframe(parts_meta)

# Simple value score calculation
st.header("💡 Value Score Calculator")
selected_cpu = st.selectbox("Choose CPU", cpus["name"])
selected_gpu = st.selectbox("Choose GPU", gpus["name"])

cpu_price = cpus.loc[cpus["name"] == selected_cpu, "price"].values[0]
gpu_price = gpus.loc[gpus["name"] == selected_gpu, "price"].values[0]
cpu_score = cpus.loc[cpus["name"] == selected_cpu, "score"].values[0]
gpu_score = gpus.loc[gpus["name"] == selected_gpu, "fps_1080p"].values[0]

value_score = round(((cpu_score / cpu_price) + (gpu_score / gpu_price)) * 10, 2)
st.metric("Total Value Score", value_score, "/100")
