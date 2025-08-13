
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="PC Build Value Scoring", page_icon="💻", layout="wide")

@st.cache_data
def load_data():
    gpus = pd.read_csv("data/gpus.csv")
    cpus = pd.read_csv("data/cpus.csv")
    meta = pd.read_csv("data/parts_meta.csv")
    return gpus, cpus, meta

def minmax_norm(x, xmin, xmax):
    if xmax - xmin <= 0:
        return 0.0
    return (x - xmin) / (xmax - xmin)

def perf_per_dollar(cpu, gpu, gpus_df, cpus_df):
    # CPU normalized score per $
    cpu_ppd_raw = cpu["score"] / max(cpu["price"], 1)
    # GPU normalized fps at 1440p per $
    gpu_ppd_raw = gpu["fps_1440p"] / max(gpu["price"], 1)

    # normalize vs dataset for stability
    cpu_ppd_all = cpus_df["score"] / cpus_df["price"].clip(lower=1)
    gpu_ppd_all = gpus_df["fps_1440p"] / gpus_df["price"].clip(lower=1)

    cpu_ppd = minmax_norm(cpu_ppd_raw, cpu_ppd_all.min(), cpu_ppd_all.max())
    gpu_ppd = minmax_norm(gpu_ppd_raw, gpu_ppd_all.min(), gpu_ppd_all.max())

    return float((cpu_ppd + gpu_ppd) / 2.0), {
        "cpu_ppd_raw": float(cpu_ppd_raw),
        "gpu_ppd_raw": float(gpu_ppd_raw),
        "cpu_ppd_norm": float(cpu_ppd),
        "gpu_ppd_norm": float(gpu_ppd),
    }

def balance_score(cpu, gpu):
    # Map CPU score to an approximate FPS capability proxy
    cpu_fps_proxy = cpu["score"] / 150.0
    # Lower penalty when CPU proxy >= 90% of GPU fps @1440p
    ratio = min(cpu_fps_proxy / max(gpu["fps_1440p"], 1), 2.0)
    # Ideal around 1.0. Use a quadratic distance from 1.
    penalty = (1.0 - min(ratio, 1.0))**2 + max(0.0, ratio-1.2)**2  # penalize too weak or wildly overkill
    balance = max(0.0, 1.0 - penalty)  # 0..1
    return float(balance), {"cpu_fps_proxy": float(cpu_fps_proxy), "ratio": float(ratio), "penalty": float(penalty)}

def upgrade_score(mobo_name, psu_name, meta_df, gpu):
    # Motherboard modernity/platform proxy
    mobo = meta_df[(meta_df["category"]=="Motherbd") & (meta_df["name"]==mobo_name)].iloc[0]
    psu = meta_df[(meta_df["category"]=="PSU") & (meta_df["name"]==psu_name)].iloc[0]

    mobo_norm = mobo["score"] / 100.0

    # PSU headroom: estimate wattage from name (e.g., "750W ...")
    import re
    w_match = re.search(r"(\d+)W", psu_name)
    psu_watts = int(w_match.group(1)) if w_match else 650
    required = gpu["tdp"] * 2.0 * 0.6  # rough system draw: GPU*0.6*2 for peaks + rest of system
    headroom = (psu_watts - required) / max(psu_watts, 1)
    headroom = np.clip(headroom, 0.0, 1.0)

    return float((mobo_norm*0.5 + headroom*0.5)), {
        "mobo_norm": float(mobo_norm),
        "psu_watts": int(psu_watts),
        "required_est": float(required),
        "headroom": float(headroom)
    }

def perks_score(ram_name, storage_name, case_name, meta_df):
    ram = meta_df[(meta_df["category"]=="RAM") & (meta_df["name"]==ram_name)].iloc[0]
    sto = meta_df[(meta_df["category"]=="Storage") & (meta_df["name"]==storage_name)].iloc[0]
    cas = meta_df[(meta_df["category"]=="Case") & (meta_df["name"]==case_name)].iloc[0]
    return float((ram["score"] + sto["score"] + cas["score"]) / 300.0)

def value_score(weights, perf_norm, balance_norm, upgrade_norm, perks_norm):
    # All components expected in 0..1, weights are 0..1 that sum to 1
    return float(100.0 * (
        weights["perf"]   * perf_norm +
        weights["balance"]* balance_norm +
        weights["upgrade"]* upgrade_norm +
        weights["perks"]  * perks_norm
    ))

def suggestions_for_gpu(selected_gpu, gpus_df):
    # Identify better price-per-frame (1440p) alternatives in similar tier
    g = selected_gpu
    ppF = g["fps_1440p"] / g["price"]
    gpus_df = gpus_df.copy()
    gpus_df["ppF"] = gpus_df["fps_1440p"] / gpus_df["price"]
    median_ppF = gpus_df["ppF"].median()

    # "Poor value" if below 0.9x median
    poor_value = ppF < 0.9 * median_ppF

    # candidates: same or adjacent tier and at least 5% better ppF
    tier_map = {t:i for i,t in enumerate(gpus_df["tier"].unique())}
    t_idx = tier_map[g["tier"]]
    candidates = gpus_df[(gpus_df["ppF"] >= ppF * 1.05) & 
                         (gpus_df["tier"].map(tier_map).between(t_idx-1, t_idx+1))]\
                         .sort_values("ppF", ascending=False).head(3)

    return poor_value, candidates[["name","price","fps_1440p","ppF","tier"]]

gpus_df, cpus_df, meta_df = load_data()

st.title("💻 PC Build Value Scoring")
st.caption("Pick parts, set prices (optional), and get an instant Value Score with friendly explanations and alternatives.")

with st.sidebar:
    st.header("Weights")
    perf_w = st.slider("Performance per $", 0.0, 1.0, 0.50, 0.05)
    bal_w  = st.slider("Balance",            0.0, 1.0, 0.25, 0.05)
    upg_w  = st.slider("Upgrade potential",  0.0, 1.0, 0.15, 0.05)
    perk_w = st.slider("Perks",              0.0, 1.0, 0.10, 0.05)
    total_w = perf_w + bal_w + upg_w + perk_w
    if abs(total_w - 1.0) > 1e-6:
        st.warning(f"Weights sum to {total_w:.2f}. They will be normalized to 1.0.")
    # normalize
    s = perf_w + bal_w + upg_w + perk_w
    weights = { "perf": perf_w/s, "balance": bal_w/s, "upgrade": upg_w/s, "perks": perk_w/s }

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("CPU")
    cpu_name = st.selectbox("Choose CPU", options=cpus_df["name"], index=1)
    cpu = cpus_df[cpus_df["name"]==cpu_name].iloc[0]
    cpu_price = st.number_input("Override CPU price ($)", value=float(cpu["price"]), step=5.0)

with col2:
    st.subheader("GPU")
    gpu_name = st.selectbox("Choose GPU", options=gpus_df["name"], index=6)
    gpu = gpus_df[gpus_df["name"]==gpu_name].iloc[0]
    gpu_price = st.number_input("Override GPU price ($)", value=float(gpu["price"]), step=10.0)

with col3:
    st.subheader("Other Parts")
    ram_name = st.selectbox("RAM", options=meta_df[meta_df["category"]=="RAM"]["name"], index=2)
    storage_name = st.selectbox("Storage", options=meta_df[meta_df["category"]=="Storage"]["name"], index=1)
    mobo_name = st.selectbox("Motherboard", options=meta_df[meta_df["category"]=="Motherbd"]["name"], index=1)
    psu_name = st.selectbox("PSU", options=meta_df[meta_df["category"]=="PSU"]["name"], index=1)
    case_name = st.selectbox("Case", options=meta_df[meta_df["category"]=="Case"]["name"], index=0)

# Apply price overrides
cpu = cpu.copy(); cpu["price"] = cpu_price
gpu = gpu.copy(); gpu["price"] = gpu_price

# Compute components
perf_norm, perf_debug = perf_per_dollar(cpu, gpu, gpus_df, cpus_df)
bal_norm, bal_debug   = balance_score(cpu, gpu)
upg_norm, upg_debug   = upgrade_score(mobo_name, psu_name, meta_df, gpu)
perks_norm            = perks_score(ram_name, storage_name, case_name, meta_df)
score = value_score(weights, perf_norm, bal_norm, upg_norm, perks_norm)
score_int = int(round(min(100, max(0, score))))

# Price total
ram = meta_df[(meta_df["category"]=="RAM") & (meta_df["name"]==ram_name)].iloc[0]
sto = meta_df[(meta_df["category"]=="Storage") & (meta_df["name"]==storage_name)].iloc[0]
mob = meta_df[(meta_df["category"]=="Motherbd") & (meta_df["name"]==mobo_name)].iloc[0]
psu = meta_df[(meta_df["category"]=="PSU") & (meta_df["name"]==psu_name)].iloc[0]
cas = meta_df[(meta_df["category"]=="Case") & (meta_df["name"]==case_name)].iloc[0]

total_price = float(cpu["price"] + gpu["price"] + ram["price"] + sto["price"] + mob["price"] + psu["price"] + cas["price"])

st.markdown("---")
st.subheader("Results")

cA, cB, cC, cD, cE = st.columns([1,1,1,1,2])
cA.metric("Value Score", f"{score_int}/100")
cB.metric("Est. 1080p FPS", f"{int(gpu['fps_1080p'])}")
cC.metric("Est. 1440p FPS", f"{int(gpu['fps_1440p'])}")
cD.metric("Est. 4K FPS", f"{int(gpu['fps_4k'])}")
cE.metric("Total Price", f"${total_price:,.0f}")

st.markdown("### Friendly Summary")
tier = gpu["tier"]
if score_int >= 85:
    verdict = "Excellent value — a sweet spot build."
elif score_int >= 70:
    verdict = "Good value — balanced for 1440p gaming."
elif score_int >= 55:
    verdict = "Decent — playable, but there are smarter swaps."
else:
    verdict = "Poor value — you're paying too much for the performance."
st.write(f"**{verdict}** This build targets **{tier}** performance. Expect smooth play at **1440p** on **High/Ultra** in most modern games, with very high FPS in esports titles.")

# Alternatives
poor_value, candidates = suggestions_for_gpu(gpu, gpus_df)
if poor_value and len(candidates) > 0:
    st.warning("Your selected GPU looks **poor value** vs. the market median. Consider these alternatives with better price-per-frame:")
    st.dataframe(candidates.reset_index(drop=True))
else:
    st.info("Your GPU choice looks **fair** or **good** value vs. similar options.")

# Advanced details expander
with st.expander("See how your score was calculated"):
    st.write("**Weights:**", weights)
    st.write("**Performance/$ (normalized)**:", perf_norm, perf_debug)
    st.write("**Balance (normalized)**:", bal_norm, bal_debug)
    st.write("**Upgrade potential (normalized)**:", upg_norm, upg_debug)
    st.write("**Perks (normalized)**:", perks_norm)

st.caption("Tip: Update prices in the sidebar overrides or edit the CSVs in `data/` for your region. All numbers here are illustrative and can be tuned.")
