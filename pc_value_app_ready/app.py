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
    ["NVIDIA RTX 5090", 60000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5090"],
    ["NVIDIA RTX 5080", 50000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5080"],
    ["NVIDIA RTX 5070 Ti", 40000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070+Ti"],
    ["NVIDIA RTX 5070", 37000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070"],
    ["NVIDIA RTX 4090", 45000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4090"],
    ["NVIDIA RTX 4080", 38000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4080"],
    ["NVIDIA RTX 4070 Ti", 30000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070+Ti"],
    ["NVIDIA RTX 4070", 27000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070"],
    ["NVIDIA RTX 4060 Ti", 22000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060+Ti"],
    ["NVIDIA RTX 4060", 20000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060"],
    ["NVIDIA RTX 3090 Ti", 25000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3090+Ti"],
    ["NVIDIA RTX 3090", 23000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3090"],
    ["NVIDIA RTX 3080 Ti", 21000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3080+Ti"],
    ["NVIDIA RTX 3080", 19000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3080"],
    ["NVIDIA RTX 3070 Ti", 17000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070+Ti"],
    ["NVIDIA RTX 3070", 15000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070"],
    ["NVIDIA RTX 3060 Ti", 14000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060+Ti"],
    ["NVIDIA RTX 3060", 12000, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060"],
    ["AMD RX 7900 XTX", 43000, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XTX"],
    ["AMD RX 7900 XT", 40000, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"],
    ["AMD RX 7800 XT", 30000, "https://pcpartpicker.com/search/?q=AMD+RX+7800+XT"],
    ["AMD RX 7700 XT", 25000, "https://pcpartpicker.com/search/?q=AMD+RX+7700+XT"],
    ["AMD RX 7600 XT", 18000, "https://pcpartpicker.com/search/?q=AMD+RX+7600+XT"],
    ["AMD RX 7600", 16000, "https://pcpartpicker.com/search/?q=AMD+RX+7600"],
    ["AMD RX 6900 XT", 22000, "https://pcpartpicker.com/search/?q=AMD+RX+6900+XT"],
    ["AMD RX 6800 XT", 20000, "https://pcpartpicker.com/search/?q=AMD+RX+6800+XT"],
    ["AMD RX 6800", 19000, "https://pcpartpicker.com/search/?q=AMD+RX+6800"],
    ["AMD RX 6700 XT", 15000, "https://pcpartpicker.com/search/?q=AMD+RX+6700+XT"],
    ["AMD RX 6600 XT", 12000, "https://pcpartpicker.com/search/?q=AMD+RX+6600+XT"],
    ["AMD RX 6600", 10000, "https://pcpartpicker.com/search/?q=AMD+RX+6600"],
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

st.markdown("### CPU Performance Spectrum")
fig_cpu = px.bar(
    cpus.sort_values("PassMark"),
    x="PassMark", y="name",
    orientation="h",
    title="CPU Performance (Higher is Better)",
    hover_data={"link": True, "PassMark": True}
)
st.plotly_chart(fig_cpu, use_container_width=True)

st.markdown("### GPU Performance Spectrum")
fig_gpu = px.bar(
    gpus.sort_values("score"),
    x="score", y="name",
    orientation="h",
    title="GPU Performance (Higher is Better)",
    hover_data={"link": True, "score": True}
)
st.plotly_chart(fig_gpu, use_container_width=True)
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
st.markdown("### CPU Performance Spectrum")
fig_cpu = px.bar(
    cpus.sort_values("PassMark"),
    x="PassMark", y="name",
    orientation="h",
    title="CPU Performance (Higher is Better)",
    hover_data={"link": True, "PassMark": True}
)
fig_cpu.update_yaxes(autorange="reversed")  # invert axis
st.plotly_chart(fig_cpu, use_container_width=True)

st.markdown("### GPU Performance Spectrum")
fig_gpu = px.bar(
    gpus.sort_values("score"),
    x="score", y="name",
    orientation="h",
    title="GPU Performance (Higher is Better)",
    hover_data={"link": True, "score": True}
)
fig_gpu.update_yaxes(autorange="reversed")
st.plotly_chart(fig_gpu, use_container_width=True)
