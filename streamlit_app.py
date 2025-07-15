import streamlit as st
import pandas as pd
import time
import os

# --- Config ---
st.set_page_config(page_title="Live Ageing Dashboard", layout="wide")
st.title("🧪 Live Ageing Dashboard")

# --- Refresh Interval ---
refresh_interval = 10  # seconds

# --- File Path ---
file_path = "ageing_table.xlsx"  # <- Replace with your actual file name

# --- Display Info ---
st.info(f"Live dashboard refreshes every {refresh_interval} seconds.")

# --- Infinite Refresh Loop ---
while True:
    try:
        # --- Load File ---
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)

        # --- Detect Front & Back Hardness Columns ---
        front_cols = [col for col in df.columns if 'Front Hardness' in col]
        back_cols = [col for col in df.columns if 'Back Hardness' in col]

        # --- Calculate Averages ---
        df['Avg Front Hardness'] = df[front_cols].mean(axis=1)
        df['Avg Back Hardness'] = df[back_cols].mean(axis=1)

        # --- Group by Alloy-Temper ---
        summary = df.groupby('Alloy-Temper')[['Avg Front Hardness', 'Avg Back Hardness']].mean().round(2)

        # --- Layout ---
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("📈 Hardness Chart by Alloy-Temper")
            st.bar_chart(summary)

        with col2:
            st.subheader("🔢 Summary Table")
            st.dataframe(summary)

        st.divider()

        # --- Show full table if needed ---
        with st.expander("📋 Show Full Table"):
            st.dataframe(df, use_container_width=True)

        # --- Wait and refresh ---
        time.sleep(refresh_interval)
        st.rerun()

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        break
