
# PC Build Value Scoring — Streamlit App

A lightweight **Python + Streamlit** tool that lets you pick parts and instantly see:
- A **Value Score (0–100)**
- Estimated FPS at 1080p/1440p/4K
- **Performance-per-dollar** metrics
- **Balance** checks (CPU↔GPU)
- **Upgrade potential** and **perk** scores
- **Alternatives** when a part looks like poor value

> Note: Dataset is included and editable (`data/*.csv`). You can update prices/scores anytime.

## Quick Start

1. Create a virtual environment (optional but recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open the local URL that Streamlit prints (usually http://localhost:8501).

## How Scoring Works

**Value Score (0–100)** combines:
- **Performance per dollar (50%)** — Normalized CPU score/$ and GPU FPS(1440p)/$.
- **Balance (25%)** — Penalizes mismatches where the CPU can’t keep up with the GPU (or vice versa).
- **Upgrade potential (15%)** — Based on PSU overhead and motherboard platform modernity.
- **Perks (10%)** — RAM speed, storage speed, and case airflow/thermals.

Formula (weights configurable in the UI):
```
Total = 50*PerfPerDollar + 25*Balance + 15*Upgrade + 10*Perks
```
(Each term is normalized to 0–1 before weighting.)

## Editing Data

- **GPUs:** `data/gpus.csv` has 1080p/1440p/4K FPS, price, TDP, tier.
- **CPUs:** `data/cpus.csv` has a CPU score (PassMark-like), price, and platform.
- **Other parts:** `data/parts_meta.csv` stores RAM, storage, motherboard, PSU, case with a simple 0–100 score.

Change prices or add new parts, then refresh the app.

## License
MIT
