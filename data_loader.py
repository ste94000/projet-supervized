import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("./dataset_final.csv").drop(columns="Unnamed: 0")
    return df
