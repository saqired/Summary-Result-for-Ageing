import streamlit as st
import pandas as pd

st.title("🧪 Google Sheet Test")

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuotFDwz3Gs5cVnYjcMhPovYHUpMsVe6LdHHUIDSJcYVVfII1pVWBXZUriMqEbim6Bs8diKBn9glc7/pub?output=csv"

try:
    df = pd.read_csv(sheet_url)
    st.success("✅ Successfully loaded Google Sheet!")
    st.dataframe(df)
except Exception as e:
    st.error(f"❌ Error: {e}")
