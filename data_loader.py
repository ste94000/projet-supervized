import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/dataset_final.csv")
    return df
