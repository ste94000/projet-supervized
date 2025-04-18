import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("./dataset_final_3.csv").drop(columns=["Unnamed: 0.1","Unnamed: 0"])
    return df

@st.cache_data
def load_data_engagement():
    df = pd.read_csv("./data_explorateur_engagement.csv")
    return df
