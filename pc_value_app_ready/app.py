import streamlit as st
import pandas as pd
import plotly.express as px

# =======================
# Component Data
# =======================

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
    ["AMD Ryzen 3 3100", 11211, "https://pcpartpicker.com/search/?q=AMD+Ryzen+3+3100"],
]
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

# Convert to DataFrames
cpus = pd.DataFrame(cpu_data, columns=["name", "PassMark", "link"])
gpus = pd.DataFrame(gpu_data, columns=["name", "score", "link"])

# =======================
# Game Requirements
# =======================
games = {
    "Cyberpunk 2077": {"cpu": 20000, "gpu": 30000},
    "The Sims 4": {"cpu": 8000, "gpu": 6000},
    "Elden Ring": {"cpu": 15000, "gpu": 25000},
    "GTA V": {"cpu": 12000, "gpu": 15000},
}

quality_multipliers = {"Low": 1, "Medium": 1.5, "High": 2, "Ultra": 3}

# =======================
# Streamlit App
# =======================
st.title("PC Build Performance Explorer")

st.sidebar.header("Choose Games and Quality")
selected_games = st.sidebar.multiselect("Select Games:", list(games.keys()))
selected_quality = st.sidebar.selectbox("Select Quality:", list(quality_multipliers.keys()))

# =======================
# Recommendations
# =======================
if selected_games:
    st.subheader("Recommended Components")
    for game in selected_games:
        req = games[game]
        multiplier = quality_multipliers[selected_quality]
        cpu_min = req["cpu"] * multiplier
        gpu_min = req["gpu"] * multiplier

        cpu_cap = cpu_min * 1.5
        gpu_cap = gpu_min * 1.5

        recommended_cpus = cpus[(cpus["PassMark"] >= cpu_min) & (cpus["PassMark"] <= cpu_cap)].nsmallest(4, "PassMark")
        recommended_gpus = gpus[(gpus["score"] >= gpu_min) & (gpus["score"] <= gpu_cap)].nsmallest(4, "score")

        st.markdown(f"**{game} ({selected_quality})**")
        st.write("CPUs:")
        for _, row in recommended_cpus.iterrows():
            st.markdown(f"- [{row['name']}]({row['link']}) ({row['PassMark']})")
        st.write("GPUs:")
        for _, row in recommended_gpus.iterrows():
            st.markdown(f"- [{row['name']}]({row['link']}) ({row['score']})")

# =======================
# Performance Graphs
# =======================
# GPU graph
gpu_fig = px.bar(
    gpu_df.sort_values("score", ascending=False),
    x="score",
    y="name",
    orientation="h",
    title="GPU Performance",
    hover_data=["link"],
)
gpu_fig.update_layout(
    yaxis=dict(categoryorder="total ascending")  # best GPUs at the top
)

# CPU graph
cpu_fig = px.bar(
    cpu_df.sort_values("score", ascending=False),
    x="score",
    y="name",
    orientation="h",
    title="CPU Performance",
    hover_data=["link"],
)
cpu_fig.update_layout(
    yaxis=dict(categoryorder="total ascending")  # best CPUs at the top
)
