import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# GPU data (FPS-based strength)
# -----------------------------
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

# -----------------------------
# CPU data (Passmark-based)
# -----------------------------
cpu_data = [
    ["AMD Ryzen 9 9950X3D", 70102], ["Intel Core Ultra 9 285K", 67488],
    ["Intel Core Ultra 7 265K", 58853], ["Intel Core i9-14900K", 57623],
    ["Intel Core i9-14900KF", 57473], ["Intel Core i9-13900K", 56805],
    ["Intel Core i9-13900KF", 56612], ["AMD Ryzen 9 7950X", 61652],
    ["AMD Ryzen 9 7900X", 50991], ["AMD Ryzen 9 5950X", 44864],
    ["AMD Ryzen 9 5900X", 38430], ["AMD Ryzen 7 9800X3D", 39926],
    ["AMD Ryzen 7 7800X3D", 34373], ["Intel Core i7-14700KF", 52027],
    ["Intel Core i7-14700K", 51530], ["Intel Core i7-13700K", 43935],
    ["Intel Core i7-12700K", 33539], ["AMD Ryzen 7 9700X", 37089],
    ["AMD Ryzen 7 7700X", 35120], ["AMD Ryzen 7 7700", 34534],
    ["AMD Ryzen 7 5700X3D", 26279], ["AMD Ryzen 7 5700X", 26522],
    ["AMD Ryzen 7 5800X3D", 28344], ["AMD Ryzen 7 5800XT", 27964],
    ["AMD Ryzen 7 5800X", 27263], ["AMD Ryzen 7 3700X", 21995],
    ["Intel Core i5-14600KF", 38421], ["Intel Core i5-14600K", 38929],
    ["Intel Core i5-13600KF", 36981], ["Intel Core i5-13600K", 37308],
    ["Intel Core i5-12600KF", 28008], ["Intel Core i5-12600K", 27301],
    ["Intel Core i5-12400F", 19506], ["Intel Core i5-12400", 16340],
    ["AMD Ryzen 5 9600X", 29934], ["AMD Ryzen 5 8600G", 25111],
    ["AMD Ryzen 5 7600X", 28095], ["AMD Ryzen 5 7600", 26966],
    ["AMD Ryzen 5 7500F", 26815], ["AMD Ryzen 5 5600X", 21727],
    ["AMD Ryzen 5 5600", 21472], ["AMD Ryzen 5 5600G", 18965],
    ["AMD Ryzen 5 5500", 19217], ["AMD Ryzen 5 3600X", 17856],
    ["AMD Ryzen 5 3600", 17529], ["Intel Core i3-12100F", 13885],
    ["Intel Core i3-12100", 9624], ["AMD Ryzen 3 3300X", 13471], ["AMD Ryzen 3 3100", 11211]
]

gpus = pd.DataFrame(gpu_data, columns=["name", "avg_fps", "low_1_percent"])
cpus = pd.DataFrame(cpu_data, columns=["name", "passmark_score"])

# -----------------------------
# Game thresholds
# -----------------------------
game_requirements = {
    "Elden Ring": {"ultra": 70, "high": 55, "medium": 45},
    "Cyberpunk 2077": {"ultra": 75, "high": 60, "medium": 55},
    "Baldur's Gate 3": {"ultra": 65, "high": 50, "medium": 50},
    "Fortnite": {"ultra": 55, "high": 45, "medium": 30},
    "Valorant": {"ultra": 50, "high": 35, "medium": 20},
    "Minecraft (Java)": {"ultra": 30, "high": 20, "medium": 10},
    "The Sims 4": {"ultra": 40, "high": 25, "medium": 15},
    "CS2 / CS:GO": {"ultra": 45, "high": 30, "medium": 20},
    "GTA V": {"ultra": 60, "high": 45, "medium": 30},
    "League of Legends": {"ultra": 35, "high": 20, "medium": 10}
}

# return a colour+label
def colour_label(game, fps):
    thr = game_requirements[game]
    if fps >= thr["ultra"]:
        return '<span style="color:#007f00">🟢 Ultra</span>'
    if fps >= thr["high"]:
        return '<span style="color:#f5bd00">🟡 High</span>'
    if fps >= thr["medium"]:
        return '<span style="color:#ff7700">🟠 Medium</span>'
    return '<span style="color:#cc0000">🔴 Low</span>'

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("PC Gaming Build Predictor")

gpu_choice = st.selectbox("Select GPU", gpus["name"])
cpu_choice = st.selectbox("Select CPU", cpus["name"])

gpu_fps = gpus.loc[gpus["name"]==gpu_choice,"avg_fps"].iat[0]
cpu_pm  = cpus.loc[cpus["name"]==cpu_choice,"passmark_score"].iat[0]

# -----------------------------
# Game colour predictions
# -----------------------------
st.subheader("Estimated Game Graphics Settings:")
for g in game_requirements:
    st.markdown(f"- **{g}** — {colour_label(g, gpu_fps)}", unsafe_allow_html=True)

# -----------------------------
# Bottleneck detection
# -----------------------------
gpu_norm = gpu_fps / 200
cpu_norm = cpu_pm  / 60000
ratio    = gpu_norm / cpu_norm

if ratio > 1.4 or ratio < 0.6:
    st.warning("⚠️ Your CPU and GPU are unbalanced (potential bottleneck).")
    if ratio > 1:
        target = gpu_norm*60000
        can = cpus.copy(); can["diff"]=(can["passmark_score"]-target).abs()
        better = can.sort_values("diff").head(3)
        st.write("Suggested CPUs instead:")
        for _,r in better.iterrows():
            st.markdown(f"- {r['name']} ({r['passmark_score']})" )
    else:
        target = cpu_norm*200
        can = gpus.copy(); can["diff"]=(can["avg_fps"]-target).abs()
        better = can.sort_values("diff").head(3)
        st.write("Suggested GPUs instead:")
        for _,r in better.iterrows():
            st.markdown(f"- {r['name']} ({r['avg_fps']})" )

# -----------------------------
# GPU scatter (value overview)
# -----------------------------
gpu_df = gpus.copy()
gpu_df['selected'] = gpu_df['name'] == gpu_choice
gpu_fig = px.scatter(
    gpu_df,
    x='avg_fps',
    y='name',
    color='selected',
    color_discrete_map={True:'#E94F37', False:'#4ECDC4'},
    title='GPU Performance (FPS)'
)
gpu_fig.update_layout(
    height=1200,  # height of graph
    width=800, # width of graph
    showlegend=False,
    xaxis_title="Average FPS",
    yaxis_title=""
)
gpu_fig.update_yaxes(categoryorder="total ascending")  # Worst at the bottom
st.plotly_chart(gpu_fig, use_container_width=True)

# -----------------------------
# CPU scatter
# -----------------------------
cpu_df = cpus.copy()
cpu_df['selected'] = cpu_df['name'] == cpu_choice
cpu_fig = px.scatter(
    cpu_df,
    x='passmark_score',
    y='name',
    color='selected',
    color_discrete_map={True:'#E94F37', False:'#4ECDC4'},
    title='CPU Performance (PassMark)'
)
cpu_fig.update_layout(
    height=1200,  # height of graph
    with = 800, # width of graph
    showlegend=False,
    xaxis_title="PassMark Score",
    yaxis_title=""
)
cpu_fig.update_yaxes(categoryorder="total ascending")  # Worst at the bottom
st.plotly_chart(cpu_fig, use_container_width=True)
