import streamlit as st
import pandas as pd

# --------------------------
# GPU data embedded directly
# --------------------------
gpu_data = [
    ["NVIDIA RTX 5090 FE",214.3,150.9],
    ["NVIDIA RTX 4090 Cybertank",189.6,151.6],
    ["NVIDIA RTX 5080 FE",165.1,134.4],
    ["Sapphire RX 7900 XTX Nitro",155.6,122.5],
    ["ASUS RTX 5070 Ti Prime",151.4,124.4],
    ["Sapphire RX 9070 XT Pulse",144.6,113.7],
    ["PowerColor RX 7900 XT Hellhound",133.9,106.2],
    ["Sapphire RX 9070 Pulse",133.5,101.9],
    ["ASUS RTX 4070 Ti TUF",128.3,105.9],
    ["NVIDIA RTX 5070 FE",125.6,103.1],
    ["Sapphire RX 7900 GRE Pulse",111.7,89.7],
    ["Sapphire RX 6950 XT Nitro",106.8,79.3],
    ["NVIDIA RTX 4070 FE",104.0,85.4],
    ["AMD RX 7800 XT Red",100.5,78.3],
    ["EVGA RTX 3080 FTW3 Ultra",96.8,79.8],
    ["PNY RTX 5060 Ti 16GB",92.5,76.3],
    ["XFX RX 7700 XT Black",87.3,68.4],
    ["Sapphire RX 9060 XT 16GB Pulse",85.8,67.8],
    ["NVIDIA RTX 3070 Ti FE",84.2,68.6],
    ["NVIDIA RTX 4060 Ti FE",77.8,64.7],
    ["Colorful RTX 3070 Bilibili",77.2,63.6],
    ["Gigabyte RTX 5060 Eagle OC",76.1,62.4],
    ["EVGA RTX 3060 Ti FTW3",68.2,55.5],
    ["XFX RX 6700 XT MERC Black",68.1,51.3],
    ["ASUS RTX 4060 Dual",61.7,49.4],
    ["AMD RX 7600 Red",60.4,47.4],
    ["PowerColor RX 6600 XT Red Devil",57.8,45.7],
    ["Intel Arc B580 RE",54.5,44.8],
    ["EVGA RTX 2070 Super XC Ultra",51.8,40.9],
    ["Acer Arc A770 BiFrost",51.6,43.0],
    ["EVGA RTX 3060 XC Black",51.6,41.7],
    ["EVGA RTX 2070",50.7,41.1],
    ["Sparkle Arc A750 Titan",49.2,40.9],
    ["XFX RX 6600 CORE",48.9,38.7],
    ["EVGA RTX 2060 KO",39.8,31.6],
    ["EVGA RTX 3050 XC Black",37.8,30.4],
    ["EVGA GTX 1070 SC",30.9,24.4],
    ["EVGA GTX 1060 SSC",22.6,17.8]
]

# --------------------------
# CPU data embedded directly
# --------------------------
cpu_data = [
    ["Intel Core i9-14900K", 4250],
    ["Intel Core i9-13900K", 4100],
    ["Intel Core i7-14700K", 3900],
    ["Intel Core i7-13700K", 3700],
    ["Intel Core i5-14600K", 3500],
    ["Intel Core i5-13600K", 3300],
    ["AMD Ryzen 9 7950X", 4200],
    ["AMD Ryzen 9 7900X", 4000],
    ["AMD Ryzen 7 7700X", 3700],
    ["AMD Ryzen 5 7600X", 3400],
    ["AMD Ryzen 9 5950X", 4000],
    ["AMD Ryzen 9 5900X", 3800],
    ["AMD Ryzen 7 5800X3D", 3600],
    ["AMD Ryzen 7 5800X", 3500],
    ["AMD Ryzen 5 5600X", 3200]
]

# Convert to DataFrames
gpus = pd.DataFrame(gpu_data, columns=["name", "avg_fps", "low_1_percent"])
cpus = pd.DataFrame(cpu_data, columns=["name", "score"])

# --------------------------
# Streamlit UI
# --------------------------
st.title("PC Value Checker")

st.header("GPU Performance")
gpu_choice = st.selectbox("Select your GPU", gpus["name"].tolist())
if gpu_choice in gpus["name"].values:
    gpu_info = gpus[gpus["name"] == gpu_choice].iloc[0]
    st.write(f"**Average FPS:** {gpu_info['avg_fps']}")
    st.write(f"**1% Low FPS:** {gpu_info['low_1_percent']}")
else:
    st.error("GPU not found in dataset.")

st.header("CPU Performance")
cpu_choice = st.selectbox("Select your CPU", cpus["name"].tolist())
if cpu_choice in cpus["name"].values:
    cpu_info = cpus[cpus["name"] == cpu_choice].iloc[0]
    st.write(f"**Benchmark Score:** {cpu_info['score']}")
else:
    st.error("CPU not found in dataset.")
