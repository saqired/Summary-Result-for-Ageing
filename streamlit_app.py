import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Live Defect Dashboard", layout="centered")
st.title("🛠️ Live Defect Dashboard (Google Sheet Connected)")

# Google Sheets CSV export link
sheet_url = sheet_url = (
    "https://docs.google.com/spreadsheets/d/"
    "2PACX-1vRuotFDwz3Gs5cVnYjcMhPovYHUpMsVe6LdHHUIDSJcYVVfII1pVWBXZUriMqEbim6Bs8diKBn9glc7"
    "/export?format=csv"
)

refresh_interval = 10
st.caption(f"⏱ Auto-refreshes every {refresh_interval} seconds")

# Refresh loop
while True:
    try:
        df = pd.read_csv(sheet_url)

        # Bar chart format
        df_defect = df[['Defect', 'Total']].set_index('Defect')
        st.subheader("📈 Total Number vs. Defects")
        st.bar_chart(df_defect)

        st.subheader("📋 Full Defect Table")
        st.dataframe(df, use_container_width=True)

        st.toast("🔁 Refreshed")
        time.sleep(refresh_interval)
        st.rerun()

    except Exception as e:
        st.error(f"Failed to load data: {e}")
        break
