import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# Component Performance Data
# ===============================
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
    ["Intel Core i3-12100", 9624], ["AMD Ryzen 3 3300X", 13471],
    ["AMD Ryzen 3 3100", 11211]
]

gpu_data = [
    ["NVIDIA RTX 5090", 60000], ["NVIDIA RTX 5080", 50000],
    ["NVIDIA RTX 5070 Ti", 40000], ["NVIDIA RTX 5070", 37000],
    ["NVIDIA RTX 4090", 45000], ["NVIDIA RTX 4080", 38000],
    ["NVIDIA RTX 4070 Ti", 30000], ["NVIDIA RTX 4070", 27000],
    ["NVIDIA RTX 4060 Ti", 22000], ["NVIDIA RTX 4060", 20000],
    ["NVIDIA RTX 3090 Ti", 25000], ["NVIDIA RTX 3090", 23000],
    ["NVIDIA RTX 3080 Ti", 21000], ["NVIDIA RTX 3080", 19000],
    ["NVIDIA RTX 3070 Ti", 17000], ["NVIDIA RTX 3070", 15000],
    ["NVIDIA RTX 3060 Ti", 14000], ["NVIDIA RTX 3060", 12000],
    ["AMD RX 7900 XTX", 43000], ["AMD RX 7900 XT", 40000],
    ["AMD RX 7800 XT", 30000], ["AMD RX 7700 XT", 25000],
    ["AMD RX 7600 XT", 18000], ["AMD RX 7600", 16000],
    ["AMD RX 6900 XT", 22000], ["AMD RX 6800 XT", 20000],
    ["AMD RX 6800", 19000], ["AMD RX 6700 XT", 15000],
    ["AMD RX 6600 XT", 12000], ["AMD RX 6600", 10000]
]

# Turn into DataFrames
cpus = pd.DataFrame(cpu_data, columns=["name", "PassMark"])
gpus = pd.DataFrame(gpu_data, columns=["name", "score"])

# ===============================
# PCPartPicker Search Links
# ===============================
lookup_links = {}

for cpu in cpus["name"]:
    query = cpu.replace(" ", "+")
    lookup_links[cpu] = f"https://pcpartpicker.com/search/?q={query}"

for gpu in gpus["name"]:
    query = gpu.replace(" ", "+")
    lookup_links[gpu] = f"https://pcpartpicker.com/search/?q={query}"

# ===============================
# Game Requirements (simplified)
# ===============================
game_requirements = {
    "Cyberpunk 2077": {"ultra": 45000, "high": 30000, "medium": 20000},
    "Elden Ring": {"ultra": 35000, "high": 25000, "medium": 18000},
    "GTA V": {"ultra": 30000, "high": 22000, "medium": 15000},
    "The Sims 4": {"ultra": 12000, "high": 8000, "medium": 6000},
    "Minecraft": {"ultra": 10000, "high": 7000, "medium": 5000}
}

# ===============================
# Helper Functions
# ===============================
def recommend_components(game, quality):
    thr = game_requirements[game][quality]
    cap = int(thr * 1.5)  # 50% higher cap
    
    gpu_recs = gpus[(gpus["score"] >= thr) & (gpus["score"] <= cap)].nsmallest(4, "score")
    cpu_recs = cpus[(cpus["PassMark"] >= thr) & (cpus["PassMark"] <= cap)].nsmallest(4, "PassMark")
    
    return gpu_recs, cpu_recs

# ===============================
# Streamlit App Layout
# ===============================
st.title("PC Part Performance & Recommendations")

game_choice = st.selectbox("Select a game", list(game_requirements.keys()))
quality_choice = st.selectbox("Select quality", ["ultra", "high", "medium"])

if st.button("Get Recommendations"):
    gpu_recs, cpu_recs = recommend_components(game_choice, quality_choice)

    st.subheader("Recommended GPUs")
    for _, row in gpu_recs.iterrows():
        name = row["name"]
        url = lookup_links.get(name, "#")
        st.markdown(f"- [{name}]({url}) — Score: {row['score']}")

    st.subheader("Recommended CPUs")
    for _, row in cpu_recs.iterrows():
        name = row["name"]
        url = lookup_links.get(name, "#")
        st.markdown(f"- [{name}]({url}) — PassMark: {row['PassMark']}")

# ===============================
# Scatter Graphs with Links
# ===============================
st.subheader("CPU Performance Spectrum")
cpus["link"] = cpus["name"].apply(lambda x: lookup_links[x])
cpus["hover"] = cpus.apply(lambda r: f"<a href='{r['link']}' target='_blank'>{r['name']}</a><br>PassMark: {r['PassMark']}", axis=1)

fig_cpu = px.scatter(cpus, x="name", y="PassMark", title="CPU PassMark Scores", size="PassMark", hover_name="name", hover_data={"hover": True, "name": False})
fig_cpu.update_traces(hovertemplate="%{customdata[0]}")
st.plotly_chart(fig_cpu, use_container_width=True)

st.subheader("GPU Performance Spectrum")
gpus["link"] = gpus["name"].apply(lambda x: lookup_links[x])
gpus["hover"] = gpus.apply(lambda r: f"<a href='{r['link']}' target='_blank'>{r['name']}</a><br>Score: {r['score']}", axis=1)

fig_gpu = px.scatter(gpus, x="name", y="score", title="GPU Scores", size="score", hover_name="name", hover_data={"hover": True, "name": False})
fig_gpu.update_traces(hovertemplate="%{customdata[0]}")
st.plotly_chart(fig_gpu, use_container_width=True)
