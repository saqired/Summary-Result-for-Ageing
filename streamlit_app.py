import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Ageing Table Summary", layout="wide")
st.title("🧪 Ageing Table Summary")

# --- File Upload ---
uploaded_file = st.file_uploader("📤 Upload your Ageing Table (Excel format)", type=["xlsx", "xls", "csv"])

if uploaded_file:
    # Read Excel or CSV
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # --- Display Full Table ---
    st.subheader("📋 Full Ageing Table")
    st.dataframe(df, use_container_width=True)

    # --- Select hardness columns automatically ---
    front_cols = [col for col in df.columns if 'Front Hardness' in col]
    back_cols = [col for col in df.columns if 'Back Hardness' in col]

    # --- Calculate average hardness ---
    df['Avg Front Hardness'] = df[front_cols].mean(axis=1)
    df['Avg Back Hardness'] = df[back_cols].mean(axis=1)

    # --- Group by Alloy-Temper and average ---
    grouped = df.groupby('Alloy-Temper')[['Avg Front Hardness', 'Avg Back Hardness']].mean().round(2)

    st.subheader("📊 Average Hardness per Alloy-Temper")
    st.dataframe(grouped)

    # --- Bar Chart using Streamlit native chart ---
    st.bar_chart(grouped)

else:
    st.info("Please upload a file to display the chart and table.")
