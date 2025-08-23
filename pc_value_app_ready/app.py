import streamlit as st
import pandas as pd

# Try Plotly (falls back gracefully with a message if not installed)
try:
    import plotly.express as px
    PLOTLY_OK = True
except Exception:
    PLOTLY_OK = False

st.set_page_config(page_title="Game-first PC Build Recommender", layout="wide")

# -----------------------------
# GPU data (FPS-based strength)
# -----------------------------
gpu_data = [
    ["NVIDIA RTX 5090 FE",214.3],
    ["NVIDIA RTX 4090 Cybertank",189.6],
    ["NVIDIA RTX 5080 FE",165.1],
    ["Sapphire RX 7900 XTX Nitro",155.6],
    ["ASUS RTX 5070 Ti Prime",151.4],
    ["Sapphire RX 9070 XT Pulse",144.6],
    ["PowerColor RX 7900 XT Hellhound",133.9],
    ["Sapphire RX 9070 Pulse",133.5],
    ["ASUS RTX 4070 Ti TUF",128.3],
    ["NVIDIA RTX 5070 FE",125.6],
    ["Sapphire RX 7900 GRE Pulse",111.7],
    ["Sapphire RX 6950 XT Nitro",106.8],
    ["NVIDIA RTX 4070 FE",104.0],
    ["AMD RX 7800 XT Red",100.5],
    ["EVGA RTX 3080 FTW3 Ultra",96.8],
    ["PNY RTX 5060 Ti 16GB",92.5],
    ["XFX RX 7700 XT Black",87.3],
    ["Sapphire RX 9060 XT 16GB Pulse",85.8],
    ["NVIDIA RTX 3070 Ti FE",84.2],
    ["NVIDIA RTX 4060 Ti FE",77.8],
    ["Colorful RTX 3070 Bilibili",77.2],
    ["Gigabyte RTX 5060 Eagle OC",76.1],
    ["EVGA RTX 3060 Ti FTW3",68.2],
    ["XFX RX 6700 XT MERC Black",68.1],
    ["ASUS RTX 4060 Dual",61.7],
    ["AMD RX 7600 Red",60.4],
    ["PowerColor RX 6600 XT Red Devil",57.8],
    ["Intel Arc B580 RE",54.5],
    ["EVGA RTX 2070 Super XC Ultra",51.8],
    ["Acer Arc A770 BiFrost",51.6],
    ["EVGA RTX 3060 XC Black",51.6],
    ["EVGA RTX 2070",50.7],
    ["Sparkle Arc A750 Titan",49.2],
    ["XFX RX 6600 CORE",48.9],
    ["EVGA RTX 2060 KO",39.8],
    ["EVGA RTX 3050 XC Black",37.8],
    ["EVGA GTX 1070 SC",30.9],
    ["EVGA GTX 1060 SSC",22.6]
]
gpus = pd.DataFrame(gpu_data, columns=["name", "avg_fps"])

# -----------------------------
# CPU data (Passmark-based) — full list you provided
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
cpus = pd.DataFrame(cpu_data, columns=["name", "passmark_score"])

# -----------------------------
# Game requirement thresholds
# -----------------------------
game_requirements = {
    "Elden Ring":         {"ultra": 70, "high": 55, "medium": 45},
    "Cyberpunk 2077":     {"ultra": 75, "high": 60, "medium": 55},
    "Baldur's Gate 3":    {"ultra": 65, "high": 50, "medium": 50},
    "Fortnite":           {"ultra": 55, "high": 45, "medium": 30},
    "Valorant":           {"ultra": 50, "high": 35, "medium": 20},
    "Minecraft (Java)":   {"ultra": 30, "high": 20, "medium": 10},
    "The Sims 4":         {"ultra": 40, "high": 25, "medium": 15},
    "CS2 / CS:GO":        {"ultra": 45, "high": 30, "medium": 20},
    "GTA V":              {"ultra": 60, "high": 45, "medium": 30},
    "League of Legends":  {"ultra": 35, "high": 20, "medium": 10}
}

# -----------------------------
# UI
# -----------------------------
st.title("🎮 Game-first PC Build Recommender")

tabs = st.tabs(["Recommendations", "Performance Graphs"])

# ===== Tab 1: Recommendations =====
with tabs[0]:
    selected_games = st.multiselect(
        "Select the games you want to play:",
        list(game_requirements.keys()),
        help="Pick a few titles. We'll compute the hardest requirement across them."
    )

    if selected_games:
        # hardest requirement across selected games
        reqs = {"ultra":0, "high":0, "medium":0}
        for game in selected_games:
            for tier in reqs:
                reqs[tier] = max(reqs[tier], game_requirements[game][tier])

        # GPUs that meet requirements
        ultra_gpus  = gpus[gpus["avg_fps"] >= reqs["ultra"]]
        high_gpus   = gpus[gpus["avg_fps"] >= reqs["high"]]
        medium_gpus = gpus[gpus["avg_fps"] >= reqs["medium"]]

        # Simple CPU tiers (guides)
        ultra_cpus  = cpus[cpus["passmark_score"] >= 40000]
        high_cpus   = cpus[cpus["passmark_score"] >= 25000]
        medium_cpus = cpus[cpus["passmark_score"] >= 15000]

        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("✅ Ultra")
            st.write("**GPUs:**", ", ".join(ultra_gpus["name"].head(6)))
            st.write("**CPUs:**", ", ".join(ultra_cpus["name"].head(6)))
        with c2:
            st.subheader("⚡ High")
            st.write("**GPUs:**", ", ".join(high_gpus["name"].head(6)))
            st.write("**CPUs:**", ", ".join(high_cpus["name"].head(6)))
        with c3:
            st.subheader("💰 Medium")
            st.write("**GPUs:**", ", ".join(medium_gpus["name"].head(6)))
            st.write("**CPUs:**", ", ".join(medium_cpus["name"].head(6)))

        st.caption(
            "Notes: GPU thresholds are derived from the hardest selected game. "
            "CPU tiers are simple PassMark guides (≥40k Ultra, ≥25k High, ≥15k Medium)."
        )
    else:
        st.info("Pick at least one game to see recommended hardware tiers.")

# ===== Tab 2: Performance Graphs =====
with tabs[1]:
    if not PLOTLY_OK:
        st.error("Plotly is not installed. Add `plotly` to your requirements.txt or run `pip install plotly` to see the charts.")
    else:
        left, right = st.columns(2)

        # GPU scatter (horizontal), sorted by performance
        with left:
            st.subheader("GPU Performance Spectrum")
            g_sorted = gpus.sort_values("avg_fps")
            fig_gpu = px.scatter(
                g_sorted,
                x="avg_fps", y="name",
                hover_data={"avg_fps": True, "name": True},
                labels={"avg_fps": "Relative GPU performance (avg FPS)", "name": "GPU"},
                title="All GPUs (higher is faster)",
                height=800
            )
            # If games are selected, add requirement guide lines
            if "selected_games" in locals() and selected_games:
                reqs = {"ultra":0, "high":0, "medium":0}
                for game in selected_games:
                    for tier in reqs:
                        reqs[tier] = max(reqs[tier], game_requirements[game][tier])
                fig_gpu.add_vline(x=reqs["medium"], line_dash="dot", annotation_text="Medium req", annotation_position="top")
                fig_gpu.add_vline(x=reqs["high"],   line_dash="dash", annotation_text="High req",   annotation_position="top")
                fig_gpu.add_vline(x=reqs["ultra"],  line_dash=None,   annotation_text="Ultra req",  annotation_position="top")
            st.plotly_chart(fig_gpu, use_container_width=True)
            st.caption("Hover to see exact model. Vertical lines show the hardest requirement for the games you selected (if any).")

        # CPU scatter (horizontal), sorted by PassMark
        with right:
            st.subheader("CPU Performance Spectrum (PassMark)")
            c_sorted = cpus.sort_values("passmark_score")
            fig_cpu = px.scatter(
                c_sorted,
                x="passmark_score", y="name",
                hover_data={"passmark_score": True, "name": True},
                labels={"passmark_score": "PassMark score (higher is faster)", "name": "CPU"},
                title="All CPUs (higher is faster)",
                height=800
            )
            # Guide lines for simple tiers
            fig_cpu.add_vline(x=15000, line_dash="dot", annotation_text="~Medium tier", annotation_position="top")
            fig_cpu.add_vline(x=25000, line_dash="dash", annotation_text="~High tier",   annotation_position="top")
            fig_cpu.add_vline(x=40000, line_dash=None,   annotation_text="~Ultra tier",  annotation_position="top")
            st.plotly_chart(fig_cpu, use_container_width=True)
            st.caption("Guide lines mark rough tiers used in recommendations (~15k / 25k / 40k PassMark).")
