import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# GPU + CPU Data (with links)
# ----------------------------
gpu_data = [
    {"name": "NVIDIA RTX 5090 FE", "score": 214, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5090"},
    {"name": "NVIDIA RTX 4090 Cybertank", "score": 190, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4090"},
    {"name": "NVIDIA RTX 5080 FE", "score": 165, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5080"},
    {"name": "Sapphire RX 7900 XTX Nitro", "score": 156, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7900+XTX"},
    {"name": "ASUS RTX 5070 Ti Prime", "score": 151, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070+Ti"},
    {"name": "Sapphire RX 9070 XT Pulse", "score": 145, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"},
    {"name": "PowerColor RX 7900 XT Hellhound", "score": 134, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"},
    {"name": "Sapphire RX 9070 Pulse", "score": 134, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"},
    {"name": "ASUS RTX 4070 Ti TUF", "score": 128, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070+Ti"},
    {"name": "NVIDIA RTX 5070 FE", "score": 126, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070"},
    {"name": "Sapphire RX 7900 GRE Pulse", "score": 112, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7900+GRE"},
    {"name": "Sapphire RX 6950 XT Nitro", "score": 107, "link": "https://pcpartpicker.com/search/?q=AMD+RX+6950+XT"},
    {"name": "NVIDIA RTX 4070 FE", "score": 104, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070"},
    {"name": "AMD RX 7800 XT Red", "score": 101, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7800+XT"},
    {"name": "EVGA RTX 3080 FTW3 Ultra", "score": 97, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3080"},
    {"name": "PNY RTX 5060 Ti 16GB", "score": 93, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060+Ti"},
    {"name": "XFX RX 7700 XT Black", "score": 87, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7700+XT"},
    {"name": "Sapphire RX 9060 XT Pulse", "score": 86, "link": "https://pcpartpicker.com/search/?q=AMD+RX+6800+XT"},
    {"name": "NVIDIA RTX 3070 Ti FE", "score": 84, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070+Ti"},
    {"name": "NVIDIA RTX 4060 Ti FE", "score": 78, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060+Ti"},
    {"name": "Colorful RTX 3070 Bilibili", "score": 77, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070"},
    {"name": "Gigabyte RTX 5060 Eagle OC", "score": 76, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060"},
    {"name": "EVGA RTX 3060 Ti FTW3", "score": 68, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060+Ti"},
    {"name": "XFX RX 6700 XT MERC Black", "score": 68, "link": "https://pcpartpicker.com/search/?q=AMD+RX+6700+XT"},
    {"name": "ASUS RTX 4060 Dual", "score": 62, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060"},
    {"name": "AMD RX 7600 Red", "score": 60, "link": "https://pcpartpicker.com/search/?q=AMD+RX+7600"},
    {"name": "PowerColor RX 6600 XT Red Devil", "score": 58, "link": "https://pcpartpicker.com/search/?q=AMD+RX+6600+XT"},
    {"name": "Intel Arc B580 FE", "score": 55, "link": "https://pcpartpicker.com/search/?q=Intel+Arc+B580"},
    {"name": "EVGA RTX 2070 Super XC Ultra", "score": 53, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+2070+Super"},
    {"name": "Acer Arc A770 BiForst", "score": 52, "link": "https://pcpartpicker.com/search/?q=Intel+Arc+A770"},
    {"name": "EVGA RTX 3060 XC Black", "score": 52, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060"},
    {"name": "EVGA RTX 2070 Z", "score": 51, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+2070"},
    {"name": "Sparkle Arc A750 Titan", "score": 49, "link": "https://pcpartpicker.com/search/?q=Intel+Arc+A750"},
    {"name": "XFX RX 6600 CORE", "score": 49, "link": "https://pcpartpicker.com/search/?q=AMD+RX+6600"},
    {"name": "EVGA RTX 2060 KO", "score": 40, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+2060"},
    {"name": "EVGA RTX 3050 XC Black", "score": 38, "link": "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3050"},
    {"name": "EVGA GTX 1070 SC", "score": 31, "link": "https://pcpartpicker.com/search/?q=NVIDIA+GTX+1070"},
    {"name": "EVGA GTX 1060 SSC", "score": 23, "link": "https://pcpartpicker.com/search/?q=NVIDIA+GTX+1060"},
]

cpu_data = [
    ["AMD Ryzen 9 9950X3D", 70102, "https://pcpartpicker.com/search/?q=AMD+Ryzen+9+9950X3D"],
    ["Intel Core Ultra 9 285K", 67488, "https://pcpartpicker.com/search/?q=Intel+Core+Ultra+9+285K"],
    ["Intel Core Ultra 7 265K", 58853, "https://pcpartpicker.com/search/?q=Intel+Core+Ultra+7+265K"],
    ["Intel Core i9-14900K", 57623, "https://pcpartpicker.com/search/?q=Intel+Core+i9-14900K"],
    ["Intel Core i9-14900KF", 57473, "https://pcpartpicker.com/search/?q=Intel+Core+i9-14900KF"],
    ["Intel Core i9-13900K", 56805, "https://pcpartpicker.com/search/?q=Intel+Core+i9-13900K"],
    ["Intel Core i9-13900KF", 56612, "https://pcpartpicker.com/search/?q=Intel+Core+i9-13900KF"],
    ["AMD Ryzen 9 7950X", 61652, "https://pcpartpicker.com/search/?q=AMD+Ryzen+9+7950X"],
    ["AMD Ryzen 9 7900X", 50991, "https://pcpartpicker.com/search/?q=AMD+Ryzen+9+7900X"],
    ["AMD Ryzen 9 5950X", 44864, "https://pcpartpicker.com/search/?q=AMD+Ryzen+9+5950X"],
    ["AMD Ryzen 9 5900X", 38430, "https://pcpartpicker.com/search/?q=AMD+Ryzen+9+5900X"],
    ["AMD Ryzen 7 9800X3D", 39926, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+9800X3D"],
    ["AMD Ryzen 7 7800X3D", 34373, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+7800X3D"],
    ["Intel Core i7-14700KF", 52027, "https://pcpartpicker.com/search/?q=Intel+Core+i7-14700KF"],
    ["Intel Core i7-14700K", 51530, "https://pcpartpicker.com/search/?q=Intel+Core+i7-14700K"],
    ["Intel Core i7-13700K", 43935, "https://pcpartpicker.com/search/?q=Intel+Core+i7-13700K"],
    ["Intel Core i7-12700K", 33539, "https://pcpartpicker.com/search/?q=Intel+Core+i7-12700K"],
    ["AMD Ryzen 7 9700X", 37089, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+9700X"],
    ["AMD Ryzen 7 7700X", 35120, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+7700X"],
    ["AMD Ryzen 7 7700", 34534, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+7700"],
    ["AMD Ryzen 7 5700X3D", 26279, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+5700X3D"],
    ["AMD Ryzen 7 5700X", 26522, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+5700X"],
    ["AMD Ryzen 7 5800X3D", 28344, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+5800X3D"],
    ["AMD Ryzen 7 5800XT", 27964, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+5800XT"],
    ["AMD Ryzen 7 5800X", 27263, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+5800X"],
    ["AMD Ryzen 7 3700X", 21995, "https://pcpartpicker.com/search/?q=AMD+Ryzen+7+3700X"],
    ["Intel Core i5-14600KF", 38421, "https://pcpartpicker.com/search/?q=Intel+Core+i5-14600KF"],
    ["Intel Core i5-14600K", 38929, "https://pcpartpicker.com/search/?q=Intel+Core+i5-14600K"],
    ["Intel Core i5-13600KF", 36981, "https://pcpartpicker.com/search/?q=Intel+Core+i5-13600KF"],
    ["Intel Core i5-13600K", 37308, "https://pcpartpicker.com/search/?q=Intel+Core+i5-13600K"],
    ["Intel Core i5-12600KF", 28008, "https://pcpartpicker.com/search/?q=Intel+Core+i5-12600KF"],
    ["Intel Core i5-12600K", 27301, "https://pcpartpicker.com/search/?q=Intel+Core+i5-12600K"],
    ["Intel Core i5-12400F", 19506, "https://pcpartpicker.com/search/?q=Intel+Core+i5-12400F"],
    ["Intel Core i5-12400", 16340, "https://pcpartpicker.com/search/?q=Intel+Core+i5-12400"],
    ["AMD Ryzen 5 9600X", 29934, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+9600X"],
    ["AMD Ryzen 5 8600G", 25111, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+8600G"],
    ["AMD Ryzen 5 7600X", 28095, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+7600X"],
    ["AMD Ryzen 5 7600", 26966, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+7600"],
    ["AMD Ryzen 5 7500F", 26815, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+7500F"],
    ["AMD Ryzen 5 5600X", 21727, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+5600X"],
    ["AMD Ryzen 5 5600", 21472, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+5600"],
    ["AMD Ryzen 5 5600G", 18965, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+5600G"],
    ["AMD Ryzen 5 5500", 19217, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+5500"],
    ["AMD Ryzen 5 3600X", 17856, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+3600X"],
    ["AMD Ryzen 5 3600", 17529, "https://pcpartpicker.com/search/?q=AMD+Ryzen+5+3600"],
    ["Intel Core i3-12100F", 13885, "https://pcpartpicker.com/search/?q=Intel+Core+i3-12100F"],
    ["Intel Core i3-12100", 9624, "https://pcpartpicker.com/search/?q=Intel+Core+i3-12100"],
    ["AMD Ryzen 3 3300X", 13471, "https://pcpartpicker.com/search/?q=AMD+Ryzen+3+3300X"],
    ["AMD Ryzen 3 3100", 11211, "https://pcpartpicker.com/search/?q=AMD+Ryzen+3+3100"]
]

# ----------------------------
# Convert to DataFrames
# ----------------------------
gpu_df = pd.DataFrame(gpu_data, columns=["name", "score", "link"])
cpu_df = pd.DataFrame(cpu_data, columns=["name", "score", "link"])

# Add clickable names
gpu_df["label"] = gpu_df.apply(lambda row: f"[{row['name']}]({row['link']})", axis=1)
cpu_df["label"] = cpu_df.apply(lambda row: f"[{row['name']}]({row['link']})", axis=1)

# ----------------------------
# Streamlit App
# ----------------------------
st.title("PC Value Checker")

# --- GAME FILTER ---
games = ["1080p Benchmarks", "1440p Benchmarks",]
selected_game = st.selectbox("Select Game/Benchmark:", games)

# --- GPU Section ---
st.subheader("GPU Performance")

selected_gpu = st.selectbox("Highlight GPU:", gpu_df["name"].tolist())
gpu_df["highlight"] = gpu_df["name"].apply(lambda x: "Selected" if x == selected_gpu else "Other")

gpu_fig = px.bar(
    gpu_df.sort_values(by="score", ascending=False),
    x="score",
    y="label",
    color="highlight",
    color_discrete_map={"Selected": "crimson", "Other": "lightgray"},
    orientation="h",
    title=f"GPU Performance - {selected_game}",
    hover_data=["score"]
)
gpu_fig.update_layout(yaxis=dict(categoryorder="total ascending"), showlegend=False)
st.plotly_chart(gpu_fig, use_container_width=True)

# --- CPU Section ---
st.subheader("CPU Performance")

selected_cpu = st.selectbox("Highlight CPU:", cpu_df["name"].tolist())
cpu_df["highlight"] = cpu_df["name"].apply(lambda x: "Selected" if x == selected_cpu else "Other")

cpu_fig = px.bar(
    cpu_df.sort_values(by="score", ascending=False),
    x="score",
    y="label",
    color="highlight",
    color_discrete_map={"Selected": "crimson", "Other": "lightgray"},
    orientation="h",
    title=f"CPU Performance - {selected_game}",
    hover_data=["score"]
)
cpu_fig.update_layout(yaxis=dict(categoryorder="total ascending"), showlegend=False)
st.plotly_chart(cpu_fig, use_container_width=True)
