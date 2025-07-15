import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Ageing Report", layout="wide")
st.title("🔥 Ageing Oven Report Dashboard")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload Ageing Table (Excel file)", type=["xlsx", "xls"])

if uploaded_file:
    # Read Excel file
    df = pd.read_excel(uploaded_file)

    # Display the table
    st.subheader("🧾 Full Ageing Table")
    st.dataframe(df, use_container_width=True)

    # --- Optional: Filter Section ---
    st.subheader("🔍 Filter by Alloy-Temper")
    selected_alloy = st.selectbox("Choose Alloy-Temper", df['Alloy-Temper'].unique())
    filtered_df = df[df['Alloy-Temper'] == selected_alloy]
    st.write(f"Filtered rows: {len(filtered_df)}")
    st.dataframe(filtered_df, use_container_width=True)

    # --- Optional: Summary ---
    st.subheader("✅ Status Summary")
    status_counts = df[['Front Status', 'Back Status']].value_counts().reset_index(name='Count')
    st.dataframe(status_counts)

else:
    st.info("📥 Please upload the Excel file containing the Ageing data.")
