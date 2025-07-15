import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Live Dashboard", layout="wide")

st.title("🔄 Live Hardness Dashboard")

# Set refresh interval (seconds)
refresh_sec = 10

# Live update loop
while True:
    # Load your file (Excel or CSV)
    df = pd.read_excel("ageing_data.xlsx")  # update path if needed

    # Calculate average hardness by Alloy
    front_cols = [col for col in df.columns if 'Front Hardness' in col]
    back_cols = [col for col in df.columns if 'Back Hardness' in col]
    
    df['Avg Front Hardness'] = df[front_cols].mean(axis=1)
    df['Avg Back Hardness'] = df[back_cols].mean(axis=1)

    summary = df.groupby("Alloy-Temper")[['Avg Front Hardness', 'Avg Back Hardness']].mean().round(2)

    # Show chart + summary
    st.subheader("📈 Hardness by Alloy-Temper (Live)")
    st.bar_chart(summary)

    st.subheader("📋 Full Table")
    st.dataframe(df, use_container_width=True)

    # Wait and rerun
    st.info(f"🔄 Refreshing in {refresh_sec} seconds...")
    time.sleep(refresh_sec)
    st.experimental_rerun()
