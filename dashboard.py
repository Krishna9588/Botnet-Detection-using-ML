import streamlit as st
import pandas as pd

df = pd.read_csv("dataset/prediction_output.csv")
st.write("### Botnet Detection Results")
st.dataframe(df)

# To run this file
# streamlit run dashboard.py
# use this command