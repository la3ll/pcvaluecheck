import streamlit as st
import pandas as pd

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
    ["AMD Ryzen 9 9950X3D", 70102],
    ["Intel Core Ultra 9 285K", 67488],
    ["Intel Core Ultra 7 265K", 58853],
    ["Intel Core i9-14900K", 57623],
    ["Intel Core i9-14900KF", 57473],
    ["Intel Core i9-13900K", 56805],
    ["Intel Core i9-13900KF", 56612],
    ["Intel Core Ultra 7 265KF", 58707],
    ["Intel Core Ultra 9 275HX", 56663],
    ["Intel Core i9-12900K", 40463],
    ["Intel Core i9-9900K @ 3.60GHz", 17689],
    ["AMD Ryzen 9 7950X", 61652],
    ["AMD Ryzen 9 7900X", 50991],
    ["AMD Ryzen 9 5950X", 44864],
    ["AMD Ryzen 9 5900X", 38430],
    ["AMD Ryzen 9 5900HX", 21440],
    ["Intel Core i7-14700KF", 52027],
    ["Intel Core i7-14700K", 51530],
    ["Intel Core i7-13700K", 43935],
    ["Intel Core i7-12700K", 33539],
    ["Intel Core i7-14700", 40833],
    ["Intel Core i7-13700KF", 45040],
    ["Intel Core i7-12700F", 30126],
    ["Intel Core i7-10700K @ 3.80GHz", 17849],
    ["AMD Ryzen 7 9800X3D", 39926],
    ["AMD Ryzen 7 7800X3D", 34373],
    ["AMD Ryzen 7 9700X", 37089],
    ["AMD Ryzen 7 7700X", 35120],
    ["AMD Ryzen 7 7700", 34534],
    ["AMD Ryzen 7 5700X3D", 26279],
    ["AMD Ryzen 7 5700X", 26522],
    ["AMD Ryzen 7 5800X3D", 28344],
    ["AMD Ryzen 7 5800XT", 27964],
    ["AMD Ryzen 7 5800X", 27263],
    ["AMD Ryzen 7 3700X", 21995],
    ["Intel Core i5-14600KF", 38421],
    ["Intel Core i5-14600K", 38929],
    ["Intel Core i5-14500", 31987],
    ["Intel Core i5-14400F", 25829],
    ["Intel Core i5-13600KF", 36981],
    ["Intel Core i5-13600K", 37308],
    ["Intel Core i5-13400F", 24799],
    ["Intel Core i5-12600KF", 28008],
    ["Intel Core i5-12600K", 27301],
    ["Intel Core i5-12400F", 19506],
    ["Intel Core i5-12400", 16340],
    ["Intel Core i5-12500", 20184],
    ["Intel Core i5-11400F @ 2.60GHz", 16544],
    ["Intel Core i5-11400 @ 2.60GHz", 14807],
    ["Intel Core i5-10400F @ 2.90GHz", 11938],
    ["Intel Core i5-10400 @ 2.90GHz", 11625],
    ["Intel Core i5-9600K @ 3.70GHz", 10575],
    ["Intel Core i5-9400F @ 2.90GHz", 9445],
    ["AMD Ryzen 5 9600X", 29934],
    ["AMD Ryzen 5 8600G", 25111],
    ["AMD Ryzen 5 7600X", 28095],
    ["AMD Ryzen 5 7600", 26966],
    ["AMD Ryzen 5 7535HS", 17570],
    ["AMD Ryzen 5 7500F", 26815],
    ["AMD Ryzen 5 5600GT", 20219],
    ["AMD Ryzen 5 5600X", 21727],
    ["AMD Ryzen 5 5600", 21472],
    ["AMD Ryzen 5 5600G", 18965],
    ["AMD Ryzen 5 5500", 19217],
    ["AMD Ryzen 5 4600H", 13452],
    ["AMD Ryzen 5 3600X", 17856],
    ["AMD Ryzen 5 3600", 17529],
    ["AMD Ryzen 5 3500U", 6713],
    ["AMD Ryzen 3 3300X", 13471],
    ["AMD Ryzen 3 3100", 11211],
    ["Intel Core i3-12100F", 13885],
    ["Intel Core i3-12100", 9624]
]

gpus = pd.DataFrame(gpu_data, columns=["name", "avg_fps", "low_1_percent"])
cpus = pd.DataFrame(cpu_data, columns=["name", "passmark_score"])

# -----------------------------
# Combine
# -----------------------------
def score(gpu_fps, cpu_passmark):
    gpu_norm = min(gpu_fps/200*100, 100)
    cpu_norm = min(cpu_passmark/60000*100, 100)
    return round(gpu_norm*0.7 + cpu_norm*0.3, 1)

game_requirements = {
    "Elden Ring":         {"ultra": 85, "high": 70, "medium": 55},
    "Cyberpunk 2077":     {"ultra": 90, "high": 75, "medium": 60},
    "Baldur's Gate 3":    {"ultra": 80, "high": 65, "medium": 50},
    "Fortnite":           {"ultra": 70, "high": 55, "medium": 40},
    "Valorant":           {"ultra": 50, "high": 35, "medium": 20},
    "Minecraft (Java)":   {"ultra": 30, "high": 20, "medium": 10},
    "The Sims 4":         {"ultra": 40, "high": 25, "medium": 15},
    "CS2 / CS:GO":        {"ultra": 45, "high": 30, "medium": 20},
    "GTA V":             {"ultra": 60, "high": 45, "medium": 30},
    "League of Legends": {"ultra": 35, "high": 20, "medium": 10}
}

def colour_setting(game, total_score):
    thr = game_requirements[game]
    if total_score >= thr["ultra"]:
        return "<span style='color:#007f00;font-weight:bold'>Ultra</span>"  # deep green
    elif total_score >= thr["high"]:
        return "<span style='color:#e8a400;font-weight:bold'>High</span>"    # amber
    elif total_score >= thr["medium"]:
        return "<span style='color:#0074cc;font-weight:bold'>Medium</span>"  # blue
    else:
        return "<span style='color:#808080;font-weight:bold'>Low</span>"     # grey

# -----------------------------
# UI
# -----------------------------
st.title("PC Gaming Build Predictor")

gpu_choice = st.selectbox("Select GPU", gpus["name"])
cpu_choice = st.selectbox("Select CPU", cpus["name"])

gpu_fps = gpus[gpus["name"] == gpu_choice]["avg_fps"].iloc[0]
cpu_score = cpus[cpus["name"] == cpu_choice]["passmark_score"].iloc[0]

total = score(gpu_fps, cpu_score)
st.subheader(f"Combined Gaming Score: {total} / 100")

st.markdown("### 📊 **Predicted Settings**")
for game in game_requirements:
    st.markdown(f"- **{game}**: {colour_setting(game, total)}", unsafe_allow_html=True)

# Decide tiers out of 5
def cpu_tier(passmark):
    if passmark > 40000: return 5
    if passmark > 25000: return 4
    if passmark > 15000: return 3
    if passmark > 8000:  return 2
    return 1

def gpu_tier(fps):
    if fps > 175: return 5
    if fps > 125: return 4
    if fps > 75:  return 3
    if fps > 45:  return 2
    return 1

ct = cpu_tier(cpu_score)
gt = gpu_tier(gpu_fps)

if abs(ct - gt) > 2:
    st.warning("⚠️ Your CPU and GPU are mismatched in power. This can bottleneck performance.")
    
    if ct > gt:
        # Suggest stronger GPU
        better_gpu = gpus[gpus['avg_fps'] > gpu_fps].head(1)['name'].values[0]
        st.write(f"Consider matching with a stronger GPU such as **{better_gpu}**")
    else:
        # Suggest weaker GPU
        weaker_gpu = gpus[gpus['avg_fps'] < gpu_fps].tail(1)['name'].values[0]
        st.write(f"Consider matching with a more realistic GPU such as **{weaker_gpu}**")
