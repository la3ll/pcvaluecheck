import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# GPU + CPU Data (with links)
# ----------------------------
gpu_data = [
    ["NVIDIA RTX 5090 FE", 214, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5090"],
    ["NVIDIA RTX 4090 Cybertank", 190, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4090"],
    ["NVIDIA RTX 5080 FE", 165, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5080"],
    ["Sapphire RX 7900 XTX Nitro", 156, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XTX"],
    ["ASUS RTX 5070 Ti Prime", 151, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070+Ti"],
    ["Sapphire RX 9070 XT Pulse", 145, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"],
    ["PowerColor RX 7900 XT Hellhound", 134, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"],
    ["Sapphire RX 9070 Pulse", 134, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"],
    ["ASUS RTX 4070 Ti TUF", 128, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070+Ti"],
    ["NVIDIA RTX 5070 FE", 126, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070"],
    ["Sapphire RX 7900 GRE Pulse", 112, "https://pcpartpicker.com/search/?q=AMD+RX+7900+GRE"],
    ["Sapphire RX 6950 XT Nitro", 107, "https://pcpartpicker.com/search/?q=AMD+RX+6950+XT"],
    ["NVIDIA RTX 4070 FE", 104, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070"],
    ["AMD RX 7800 XT Red", 101, "https://pcpartpicker.com/search/?q=AMD+RX+7800+XT"],
    ["EVGA RTX 3080 FTW3 Ultra", 97, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3080"],
    ["PNY RTX 5060 Ti 16GB", 93, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060+Ti"],
    ["XFX RX 7700 XT Black", 87, "https://pcpartpicker.com/search/?q=AMD+RX+7700+XT"],
    ["Sapphire RX 9060 XT Pulse", 86, "https://pcpartpicker.com/search/?q=AMD+RX+6800+XT"],
    ["NVIDIA RTX 3070 Ti FE", 84, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070+Ti"],
    ["NVIDIA RTX 4060 Ti FE", 78, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060+Ti"],
    ["Colorful RTX 3070 Bilibili", 77, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070"],
    ["Gigabyte RTX 5060 Eagle OC", 76, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060"],
    ["EVGA RTX 3060 Ti FTW3", 68, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060+Ti"],
    ["XFX RX 6700 XT MERC Black", 68, "https://pcpartpicker.com/search/?q=AMD+RX+6700+XT"],
    ["ASUS RTX 4060 Dual", 62, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060"],
    ["AMD RX 7600 Red", 60, "https://pcpartpicker.com/search/?q=AMD+RX+7600"],
    ["PowerColor RX 6600 XT Red Devil", 58, "https://pcpartpicker.com/search/?q=AMD+RX+6600+XT"],
    ["Intel Arc B580 FE", 55, "https://pcpartpicker.com/search/?q=Intel+Arc+B580"],
    ["EVGA RTX 2070 Super XC Ultra", 53, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+2070+Super"],
    ["Acer Arc A770 BiForst", 52, "https://pcpartpicker.com/search/?q=Intel+Arc+A770"],
    ["EVGA RTX 3060 XC Black", 52, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060"],
    ["EVGA RTX 2070 Z", 51, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+2070"],
    ["Sparkle Arc A750 Titan", 49, "https://pcpartpicker.com/search/?q=Intel+Arc+A750"],
    ["XFX RX 6600 CORE", 49, "https://pcpartpicker.com/search/?q=AMD+RX+6600"],
    ["EVGA RTX 2060 KO", 40, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+2060"],
    ["EVGA RTX 3050 XC Black", 38, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3050"],
    ["EVGA GTX 1070 SC", 31, "https://pcpartpicker.com/search/?q=NVIDIA+GTX+1070"],
    ["EVGA GTX 1060 SSC", 23, "https://pcpartpicker.com/search/?q=NVIDIA+GTX+1060"],
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

# ----------------------------
# Game Selection
# ----------------------------
games = [
    "Cyberpunk 2077",
    "Fortnite",
    "The Last of Us Part I",
    "Resident Evil 4 Remake",
    "Counter-Strike 2",
    "Sims 4",
    "Minecraft"
]
selected_game = st.selectbox("Select Game:", games)

# ----------------------------
# Game Requirements
# ----------------------------
game_requirements = {
    "Cyberpunk 2077": {
        "ultra": {"gpu": 180, "cpu": 120},
        "high": {"gpu": 140, "cpu": 100},
        "medium": {"gpu": 100, "cpu": 70},
        "low": {"gpu": 70, "cpu": 50},
    },
    "Fortnite": {
        "ultra": {"gpu": 90, "cpu": 90},
        "high": {"gpu": 70, "cpu": 65},
        "medium": {"gpu": 45, "cpu": 45},
        "low": {"gpu": 35, "cpu": 30},
    },
    "The Last of Us Part I": {
        "ultra": {"gpu": 160, "cpu": 120},
        "high": {"gpu": 130, "cpu": 100},
        "medium": {"gpu": 100, "cpu": 75},
        "low": {"gpu": 70, "cpu": 55},
    },
    "Resident Evil 4 Remake": {
        "ultra": {"gpu": 150, "cpu": 110},
        "high": {"gpu": 110, "cpu": 90},
        "medium": {"gpu": 80, "cpu": 70},
        "low": {"gpu": 55, "cpu": 50},
    },
    "Counter-Strike 2": {
        "ultra": {"gpu": 60, "cpu": 75},
        "high": {"gpu": 45, "cpu": 65},
        "medium": {"gpu": 35, "cpu": 45},
        "low": {"gpu": 15, "cpu": 30},
    },
    "Sims 4": {
        "ultra": {"gpu": 30, "cpu": 50},
        "high": {"gpu": 25, "cpu": 40},
        "medium": {"gpu": 18, "cpu": 25},
        "low": {"gpu": 12, "cpu": 15},
    },
    "Minecraft": {
        "ultra": {"gpu": 40, "cpu": 45},
        "high": {"gpu": 30, "cpu": 35},
        "medium": {"gpu": 20, "cpu": 18},
        "low": {"gpu": 10, "cpu": 12},
    },
}

# ----------------------------
# Performance Evaluation Function
# ----------------------------
def get_performance(game, gpu_score, cpu_score):
    thresholds = game_requirements[game]

    def tier(score, reqs, part):
        if score >= reqs["ultra"][part]: return "Ultra"
        elif score >= reqs["high"][part]: return "High"
        elif score >= reqs["medium"][part]: return "Medium"
        else: return "Low"

    gpu_tier = tier(gpu_score, thresholds, "gpu")
    cpu_tier = tier(cpu_score, thresholds, "cpu")

    # Final performance = lowest of GPU or CPU tier
    tiers = ["Low", "Medium", "High", "Ultra"]
    final_tier = min(gpu_tier, cpu_tier, key=lambda t: tiers.index(t))

    return final_tier, gpu_tier, cpu_tier


# ----------------------------
# GPU Section
# ----------------------------
st.subheader("GPU Performance")

selected_gpu = st.selectbox("Highlight GPU:", gpu_df["name"].tolist())
gpu_score = gpu_df.loc[gpu_df["name"] == selected_gpu, "score"].values[0]
final_tier, gpu_tier, _ = get_performance(selected_game, gpu_score, 99999)  # CPU maxed

# Map tier colors
tier_colors = {
    "Ultra": "limegreen",
    "High": "dodgerblue",
    "Medium": "orange",
    "Low": "red",
}

gpu_df["highlight"] = gpu_df["name"].apply(lambda x: "Selected" if x == selected_gpu else "Other")
gpu_df["color"] = gpu_df["highlight"].apply(
    lambda h: tier_colors[gpu_tier] if h == "Selected" else "lightgray"
)

gpu_fig = px.bar(
    gpu_df.sort_values(by="score", ascending=False),
    x="score",
    y="label",
    color="color",
    color_discrete_map="identity",
    orientation="h",
    title=f"GPU Performance - {selected_game}",
    hover_data=["score"]
)
gpu_fig.update_layout(yaxis=dict(categoryorder="total ascending"), showlegend=False)
st.plotly_chart(gpu_fig, use_container_width=True)

# ----------------------------
# CPU Section
# ----------------------------
st.subheader("CPU Performance")

selected_cpu = st.selectbox("Highlight CPU:", cpu_df["name"].tolist())
cpu_score = cpu_df.loc[cpu_df["name"] == selected_cpu, "score"].values[0]
final_tier, _, cpu_tier = get_performance(selected_game, 99999, cpu_score)  # GPU maxed

cpu_df["highlight"] = cpu_df["name"].apply(lambda x: "Selected" if x == selected_cpu else "Other")
cpu_df["color"] = cpu_df["highlight"].apply(
    lambda h: tier_colors[cpu_tier] if h == "Selected" else "lightgray"
)

cpu_fig = px.bar(
    cpu_df.sort_values(by="score", ascending=False),
    x="score",
    y="label",
    color="color",
    color_discrete_map="identity",
    orientation="h",
    title=f"CPU Performance - {selected_game}",
    hover_data=["score"]
)
cpu_fig.update_layout(yaxis=dict(categoryorder="total ascending"), showlegend=False)
st.plotly_chart(cpu_fig, use_container_width=True)
