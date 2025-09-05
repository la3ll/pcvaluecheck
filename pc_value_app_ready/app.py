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

# ----------------------------
# Streamlit App
# ----------------------------
st.title("PC Value Checker")

# ----------------------------
# Game requirements
# ----------------------------
game_requirements = {
    "Cyberpunk 2077": {"cpu": {"low":5000,"medium":15000,"high":30000,"ultra":50000}, 
                        "gpu": {"low":50,"medium":100,"high":150,"ultra":200}},
    "Elden Ring": {"cpu": {"low":3000,"medium":10000,"high":20000,"ultra":40000}, 
                   "gpu": {"low":40,"medium":80,"high":120,"ultra":180}},
    "Minecraft": {"cpu": {"low":1000,"medium":5000,"high":15000,"ultra":30000}, 
                  "gpu": {"low":20,"medium":50,"high":80,"ultra":150}},
    "Counter Strike 2": {"cpu": {"low":1000,"medium":5000,"high":15000,"ultra":25000}, 
                         "gpu": {"low":20,"medium":50,"high":80,"ultra":120}},
    "The Sims 4": {"cpu": {"low":1000,"medium":5000,"high":15000,"ultra":25000}, 
                   "gpu": {"low":20,"medium":40,"high":60,"ultra":100}},
    "Valorant": {"cpu": {"low":1000,"medium":3000,"high":8000,"ultra":15000}, 
                 "gpu": {"low":15,"medium":30,"high":50,"ultra":80}},
}

# ----------------------------
# Game Selection
# ----------------------------
games = list(game_requirements.keys())
selected_game = st.selectbox("Select Game/Benchmark:", games)

# ----------------------------
# CPU/GPU Selection
# ----------------------------
selected_gpu = st.selectbox("Select GPU:", gpu_df["name"])
selected_cpu = st.selectbox("Select CPU:", cpu_df["name"])

# ----------------------------
# Dynamic GPU Tiering
# ----------------------------
def get_gpu_tiers(gpu_scores):
    gpu_min = gpu_scores.min()
    gpu_max = gpu_scores.max()
    gpu_range = gpu_max - gpu_min
    tiers = {
        "low": gpu_min + 0.1 * gpu_range,
        "medium": gpu_min + 0.3 * gpu_range,
        "high": gpu_min + 0.55 * gpu_range,
        "ultra": gpu_max
    }
    return tiers

# ----------------------------
# Performance Logic
# ----------------------------
def get_performance(game, gpu_score, cpu_score):
    # CPU scaling: 0–200
    cpu_min = cpu_df["score"].min()
    cpu_max = cpu_df["score"].max()
    cpu_scaled = (cpu_score - cpu_min) / (cpu_max - cpu_min) * 200

    # GPU tier
    gpu_tiers_scaled = get_gpu_tiers(gpu_df["score"])
    if gpu_score >= gpu_tiers_scaled["ultra"]:
        gpu_tier = "Ultra"
    elif gpu_score >= gpu_tiers_scaled["high"]:
        gpu_tier = "High"
    elif gpu_score >= gpu_tiers_scaled["medium"]:
        gpu_tier = "Medium"
    else:
        gpu_tier = "Low"

    # CPU tier based on game
    thresholds = game_requirements[game]

    def tier(score, reqs, part):
        if score >= reqs[part]["ultra"]:
            return "Ultra"
        elif score >= reqs[part]["high"]:
            return "High"
        elif score >= reqs[part]["medium"]:
            return "Medium"
        else:
            return "Low"

    cpu_tier = tier(cpu_scaled, thresholds, "cpu")

    # Final performance = lowest of GPU or CPU tier
    tiers_order = ["Low", "Medium", "High", "Ultra"]
    final_tier = min(gpu_tier, cpu_tier, key=lambda t: tiers_order.index(t))

    return final_tier, gpu_tier, cpu_tier, cpu_scaled

# ----------------------------
# Get selected component scores
# ----------------------------
gpu_score = gpu_df.loc[gpu_df["name"] == selected_gpu, "score"].values[0]
cpu_score = cpu_df.loc[cpu_df["name"] == selected_cpu, "score"].values[0]

final_tier, gpu_tier, cpu_tier, cpu_scaled = get_performance(
    selected_game, gpu_score, cpu_score
)

st.subheader("Performance Summary")
st.write(f"**GPU Tier:** {gpu_tier}")
st.write(f"**CPU Tier:** {cpu_tier}")
st.write(f"**Final Performance:** {final_tier}")

# ----------------------------
# GPU Chart
# ----------------------------
gpu_sorted = gpu_df.sort_values("score", ascending=True)
fig_gpu = px.bar(
    gpu_sorted,
    x="score",
    y="name",
    orientation="h",
    text="score",
    labels={"score": "GPU Score", "name": "GPU"},
    title="GPU Benchmark Comparison"
)
fig_gpu.update_traces(
    marker_color=["orange" if x==selected_gpu else "lightblue" for x in gpu_sorted["name"]],
    marker_line_color=["black" if x==selected_gpu else None for x in gpu_sorted["name"]],
    marker_line_width=[2 if x==selected_gpu else 0 for x in gpu_sorted["name"]],
)
st.plotly_chart(fig_gpu, use_container_width=True)

# ----------------------------
# CPU Chart
# ----------------------------
cpu_sorted = cpu_df.sort_values("score", ascending=True)
fig_cpu = px.bar(
    cpu_sorted,
    x="score",
    y="name",
    orientation="h",
    text="score",
    labels={"score": "CPU Score", "name": "CPU"},
    title="CPU Benchmark Comparison"
)
fig_cpu.update_traces(
    marker_color=["orange" if x==selected_cpu else "lightblue" for x in cpu_sorted["name"]],
    marker_line_color=["black" if x==selected_cpu else None for x in cpu_sorted["name"]],
    marker_line_width=[2 if x==selected_cpu else 0 for x in cpu_sorted["name"]],
)
st.plotly_chart(fig_cpu, use_container_width=True)
