import time
import streamlit as st

st.title("📊 Live Dashboard Example")

while True:
    # load data from file or API
    df = pd.read_csv("live_data.csv")
    
    st.line_chart(df)
    
    time.sleep(10)  # refresh every 10 seconds
    st.experimental_rerun()
