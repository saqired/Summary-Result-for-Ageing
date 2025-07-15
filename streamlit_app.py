import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Ageing Bar Chart", layout="centered")
st.title("📊 Average Hardness by Alloy-Temper")

# --- Simulated Data (replace this with Excel import later) ---
data = {
    'Alloy-Temper': ['6060 C80-T6', '6082-T6', '6061-T6'],
    'Avg Front Hardness': [13, 17, 16],
    'Avg Back Hardness': [13, 17, 16]
}
df_avg = pd.DataFrame(data)

# --- Show Table ---
st.subheader("🧾 Average Hardness Table")
st.dataframe(df_avg, use_container_width=True)

# --- Bar Chart: Streamlit-native ---
st.subheader("📈 Bar Chart: Average Hardness")

# Set index for bar chart
df_chart = df_avg.set_index('Alloy-Temper')

# Show bar chart
st.bar_chart(df_chart)
