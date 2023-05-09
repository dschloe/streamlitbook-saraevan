# -*- coding:utf-8 -*-
import pandas as pd

from utils import load_data
import streamlit as st

def run_home():
    total_df = load_data()
    total_df['DEAL_YMD'] = pd.to_datetime(total_df['DEAL_YMD'], format="%Y-%m-%d")
    total_df['month'] = total_df['DEAL_YMD'].dt.month
    total_df = total_df.loc[total_df['HOUSE_TYPE'] == '아파트', :]
    sgg_nm = st.sidebar.selectbox("자치구", sorted(total_df['SGG_NM'].unique()))
    col1, col2 = st.columns(2)
    with col1:
        st.title('3월')
        march = total_df[total_df['month'] == 3]
        march_min_price = march[march['SGG_NM'] == sgg_nm]['OBJ_AMT'].min()
        march_max_price = march[march['SGG_NM'] == sgg_nm]['OBJ_AMT'].max()

        st.metric(label = f"{sgg_nm} 최소가격(만원)", value = march_min_price)
        st.metric(label = f"{sgg_nm} 최대가격(만원)", value = march_max_price)

    with col2:
        st.title('4월')
        march = total_df[total_df['month'] == 4]
        march_min_price = march[march['SGG_NM'] == sgg_nm]['OBJ_AMT'].min()
        march_max_price = march[march['SGG_NM'] == sgg_nm]['OBJ_AMT'].max()

        st.metric(label = f"{sgg_nm} 최소가격(만원)", value = march_min_price)
        st.metric(label = f"{sgg_nm} 최대가격(만원)", value = march_max_price)