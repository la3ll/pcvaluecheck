import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# GPU + CPU Data (with links)
# ----------------------------
gpu_data = [
    ["NVIDIA RTX 5090", 214, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5090"],
    ["NVIDIA RTX 5080", 165, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5080"],
    ["NVIDIA RTX 4090", 189, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4090"],
    ["AMD RX 7900 XTX", 156, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XTX"],
    ["NVIDIA RTX 5070 Ti", 151, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070+Ti"],
    ["NVIDIA RTX 5070", 126, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+5070"],
    ["AMD RX 7900 XT", 134, "https://pcpartpicker.com/search/?q=AMD+RX+7900+XT"],
    ["AMD RX 7800 XT", 101, "https://pcpartpicker.com/search/?q=AMD+RX+7800+XT"],
    ["NVIDIA RTX 4070 Ti", 128, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070+Ti"],
    ["NVIDIA RTX 4070", 104, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4070"],
    ["NVIDIA RTX 4060 Ti", 78, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060+Ti"],
    ["NVIDIA RTX 4060", 72, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+4060"],
    ["NVIDIA RTX 3090 Ti", 97, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3090+Ti"],
    ["NVIDIA RTX 3090", 87, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3090"],
    ["NVIDIA RTX 3080 Ti", 85, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3080+Ti"],
    ["NVIDIA RTX 3080", 84, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3080"],
    ["NVIDIA RTX 3070 Ti", 68, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070+Ti"],
    ["NVIDIA RTX 3070", 62, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3070"],
    ["NVIDIA RTX 3060 Ti", 68, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060+Ti"],
    ["NVIDIA RTX 3060", 52, "https://pcpartpicker.com/search/?q=NVIDIA+RTX+3060"],
    ["AMD RX 7900 GRE", 112, "https://pcpartpicker.com/search/?q=AMD+RX+7900+GRE"],
    ["AMD RX 7600 XT", 61, "https://pcpartpicker.com/search/?q=AMD+RX+7600+XT"],
    ["AMD RX 7600", 60, "https://pcpartpicker.com/search/?q=AMD+RX+7600"],
    ["AMD RX 6900 XT", 107, "https://pcpartpicker.com/search/?q=AMD+RX+6900+XT"],
    ["AMD RX 6800 XT", 100, "https://pcpartpicker.com/search/?q=AMD+RX+6800+XT"],
    ["AMD RX 6800", 92, "https://pcpartpicker.com/search/?q=AMD+RX+6800"],
    ["AMD RX 6700 XT", 68, "https://pcpartpicker.com/search/?q=AMD+RX+6700+XT"],
    ["AMD RX 6600 XT", 58, "https://pcpartpicker.com/search/?q=AMD+RX+6600+XT"],
    ["AMD RX 6600", 49, "https://pcpartpicker.com/search/?q=AMD+RX+6600"]
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

# --- GPU Section ---
st.subheader("GPU Performance")

selected_gpus = st.multiselect(
    "Filter GPUs:",
    options=gpu_df["name"].tolist(),
    default=gpu_df["name"].tolist()
)
filtered_gpu_df = gpu_df[gpu_df["name"].isin(selected_gpus)]

gpu_fig = px.bar(
    filtered_gpu_df.sort_values(by="score", ascending=False),
    x="score",
    y="label",
    orientation="h",
    title="GPU Benchmark (Higher is Better)",
    hover_data=["score"]
)
gpu_fig.update_layout(yaxis=dict(categoryorder="total ascending"))
st.plotly_chart(gpu_fig, use_container_width=True)

# --- CPU Section ---
st.subheader("CPU Performance")

selected_cpus = st.multiselect(
    "Filter CPUs:",
    options=cpu_df["name"].tolist(),
    default=cpu_df["name"].tolist()
)
filtered_cpu_df = cpu_df[cpu_df["name"].isin(selected_cpus)]

cpu_fig = px.bar(
    filtered_cpu_df.sort_values(by="score", ascending=False),
    x="score",
    y="label",
    orientation="h",
    title="CPU Benchmark (Higher is Better)",
    hover_data=["score"]
)
cpu_fig.update_layout(yaxis=dict(categoryorder="total ascending"))
st.plotly_chart(cpu_fig, use_container_width=True)
