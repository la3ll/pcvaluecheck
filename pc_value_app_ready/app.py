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
    ["AMD Ryzen 7 9800X3D", 39923],
    ["AMD Ryzen 7 7800X3D", 34373],
    ["AMD Ryzen 7 5700X", 26542],
    ["AMD Ryzen 5 5600X", 21731],
    ["AMD Ryzen 9 9950X3D", 70109],
    ["AMD Ryzen 5 3600", 17530],
    ["Intel Core i9-14900K", 57643],
    ["Intel Core i5-1135G7 @ 2.40GHz", 8971],
    ["Intel Core i5-12400F", 19506],
    ["AMD Ryzen 9 5900X", 38431],
    ["AMD Ryzen 7 5800X", 27250],
    ["AMD Ryzen 5 5500", 19226],
    ["AMD Ryzen 5 7600X", 28095],
    ["AMD Ryzen 5 5600", 21470],
    ["AMD Ryzen 7 9700X", 37090],
    ["Intel Core Ultra 7 265K", 58877],
    ["Intel Core Ultra 9 285K", 67529],
    ["AMD Ryzen 5 5600G", 18972],
    ["AMD Ryzen 5 9600X", 29939],
    ["AMD Ryzen 7 3700X", 21993],
    ["AMD Ryzen 9 5950X", 44875],
    ["AMD Ryzen 7 5700X3D", 26298],
    ["AMD Ryzen 9 9950X", 65772],
    ["Intel Core Ultra 7 155H", 24466],
    ["Intel Core i7-14700K", 51557],
    ["AMD Ryzen 7 7700", 34543],
    ["AMD Ryzen 7 5700G", 24054],
    ["Intel Core i7-11800H @ 2.30GHz", 18950],
    ["Intel Core i9-14900KF", 57449],
    ["AMD Ryzen 9 9900X", 54426],
    ["Intel Core i5-12450H", 15573],
    ["Intel Core i7-12700H", 23776],
    ["Intel Core i5-1235U", 12356],
    ["Intel Core i7-12700K", 33528],
    ["AMD Ryzen 5 PRO 7645", 27574],
    ["Intel Core i7-8700 @ 3.20GHz", 12527],
    ["AMD Ryzen 7 7700X", 35122],
    ["AMD Ryzen 9 7900X", 51014],
    ["Intel Core i5-14400F", 25824],
    ["Intel Core i7-1165G7 @ 2.80GHz", 9256],
    ["Intel Core i5-1145G7 @ 2.60GHz", 8923],
    ["Intel Core i7-9750H @ 2.60GHz", 10005],
    ["Intel N97", 6064],
    ["Intel Core i9-13900K", 56777],
    ["Intel Core i7-10750H @ 2.60GHz", 10875],
    ["Intel Core i7-13620H", 23433],
    ["Intel Core i7-14700KF", 52012],
    ["AMD Ryzen 7 5800X3D", 28362],
    ["AMD Ryzen 5 7600", 26966],
    ["Intel Core i9-14900HX", 43669],
    ["Intel Core i5-8250U @ 1.60GHz", 5682],
    ["Intel Core Ultra 9 275HX", 56662],
    ["Intel Core i5-11400H @ 2.70GHz", 14908],
    ["Intel Core i5-13420H", 17038],
    ["Intel Core i7-9700K @ 3.60GHz", 14273],
    ["AMD Ryzen 7 5800H", 19749],
    ["Intel Core i9-9900K @ 3.60GHz", 17713],
    ["Intel Core i5-12400", 16296],
    ["Intel Core i3-1115G4 @ 3.00GHz", 5729],
    ["Intel Core i5-10210U @ 1.60GHz", 5759],
    ["Intel Core i5-10400F @ 2.90GHz", 11924],
    ["Intel Core i9-12900K", 40471],
    ["Intel Core i7-8750H @ 2.20GHz", 9257],
    ["Intel Core i3-12100", 9579]
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
