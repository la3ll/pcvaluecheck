# PC Value Checker

A Streamlit app to evaluate PC builds, showing performance and value scores based on realistic component data.

## How to run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## How to deploy on Streamlit Cloud
1. Upload this folder to your GitHub repo (e.g., `pc_value_app`).
2. In Streamlit Cloud, create a new app pointing to `pc_value_app/app.py`.
3. The CSVs are loaded directly from GitHub raw URLs — updating them in GitHub will update the app instantly.
