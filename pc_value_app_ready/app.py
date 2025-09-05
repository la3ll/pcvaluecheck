import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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

# Keep names clean for dropdowns
gpu_df["label"] = gpu_df["name"]
cpu_df["label"] = cpu_df["name"]

# ----------------------------
# Streamlit App
# ----------------------------
st.title("🎮 PC Value & Game Performance Checker")

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
# User Selections
# ----------------------------
selected_game = st.selectbox("Select Game:", list(game_requirements.keys()))
selected_cpu = st.selectbox("Select CPU:", cpu_df["label"])
selected_gpu = st.selectbox("Select GPU:", gpu_df["label"])

# ----------------------------
# Fetch scores and links
# ----------------------------
cpu_score = cpu_df.loc[cpu_df["label"] == selected_cpu, "score"].values[0]
gpu_score = gpu_df.loc[gpu_df["label"] == selected_gpu, "score"].values[0]

cpu_link = cpu_df.loc[cpu_df["label"] == selected_cpu, "link"].values[0]
gpu_link = gpu_df.loc[gpu_df["label"] == selected_gpu, "link"].values[0]

# Display clickable links
st.markdown(f"🔗 [CPU Link]({cpu_link})")
st.markdown(f"🔗 [GPU Link]({gpu_link})")

# ----------------------------
# Performance Logic
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

    tiers = ["Low", "Medium", "High", "Ultra"]
    final_tier = min(gpu_tier, cpu_tier, key=lambda t: tiers.index(t))

    return final_tier, gpu_tier, cpu_tier

final_tier, gpu_tier, cpu_tier = get_performance(selected_game, gpu_score, cpu_score)

# ----------------------------
# Display Results
# ----------------------------
st.subheader("🔎 Benchmark Scores")
st.write(f"**CPU**: {selected_cpu} → Score: {cpu_score}")
st.write(f"**GPU**: {selected_gpu} → Score: {gpu_score}")

st.subheader("🖥️ Component Tiers vs Game Requirements")
st.write(f"CPU Tier: **{cpu_tier}**")
st.write(f"GPU Tier: **{gpu_tier}**")

st.subheader("🎨 Expected Graphics Quality")
st.success(f"Final predicted tier for **{selected_game}**: **{final_tier}**")


# ----------------------------
# CPU Graph with Game Requirements
# ----------------------------
cpu_sorted = cpu_df.sort_values("score").copy()
cpu_sorted["Type"] = cpu_sorted["label"].apply(lambda x: "Your Part" if x == selected_cpu else "Other Parts")

fig_cpu = go.Figure()

# Add all CPU bars
fig_cpu.add_trace(go.Bar(
    x=cpu_sorted["label"],
    y=cpu_sorted["score"],
    marker_color=[ "dodgerblue" if x==selected_cpu else "lightgray" for x in cpu_sorted["label"]],
    text=cpu_sorted["score"],
    name="CPU Benchmark"
))

# Highlight selected CPU with black outline
fig_cpu.update_traces(marker_line_color=["black" if x==selected_cpu else None for x in cpu_sorted["label"]],
                      marker_line_width=[2 if x==selected_cpu else 0 for x in cpu_sorted["label"]])

# Add horizontal lines for game requirements
tiers = ["low", "medium", "high", "ultra"]
colors = ["green", "yellow", "orange", "red"]
for tier, color in zip(tiers, colors):
    req_score = game_requirements[selected_game][tier]["cpu"]
    fig_cpu.add_hline(y=req_score, line_dash="dash", line_color=color,
                       annotation_text=f"{tier.capitalize()} Requirement",
                       annotation_position="top left")

fig_cpu.update_layout(
    title=f"CPU Benchmark Scores with {selected_game} Requirements",
    xaxis_title="CPU",
    yaxis_title="Benchmark Score",
    xaxis_tickangle=-45,
    height=450,
    showlegend=False
)

st.plotly_chart(fig_cpu)

# ----------------------------
# GPU Graph with Game Requirements
# ----------------------------
gpu_sorted = gpu_df.sort_values("score").copy()
gpu_sorted["Type"] = gpu_sorted["label"].apply(lambda x: "Your Part" if x == selected_gpu else "Other Parts")

fig_gpu = go.Figure()

# Add all GPU bars
fig_gpu.add_trace(go.Bar(
    x=gpu_sorted["label"],
    y=gpu_sorted["score"],
    marker_color=[ "dodgerblue" if x==selected_gpu else "lightgray" for x in gpu_sorted["label"]],
    text=gpu_sorted["score"],
    name="GPU Benchmark"
))

# Highlight selected GPU
fig_gpu.update_traces(marker_line_color=["black" if x==selected_gpu else None for x in gpu_sorted["label"]],
                      marker_line_width=[2 if x==selected_gpu else 0 for x in gpu_sorted["label"]])

# Add horizontal lines for game requirements
for tier, color in zip(tiers, colors):
    req_score = game_requirements[selected_game][tier]["gpu"]
    fig_gpu.add_hline(y=req_score, line_dash="dash", line_color=color,
                       annotation_text=f"{tier.capitalize()} Requirement",
                       annotation_position="top left")

fig_gpu.update_layout(
    title=f"GPU Benchmark Scores with {selected_game} Requirements",
    xaxis_title="GPU",
    yaxis_title="Benchmark Score",
    xaxis_tickangle=-45,
    height=450,
    showlegend=False
)

st.plotly_chart(fig_gpu)
