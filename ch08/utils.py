# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv("data/seoul_real_estate.csv")
    return data