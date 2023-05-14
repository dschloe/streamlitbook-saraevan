# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from prophet import Prophet

def predictDistrict(total_df):

    total_df['DEAL_YMD'] = pd.to_datetime(total_df['DEAL_YMD'], format="%Y-%m-%d")
    sgg_nms = list(total_df['SGG_NM'].unique())
    periods = int(st.number_input("향후 예측 기간을 지정하세요(1일 ~ 30일)", min_value=1, max_value=30, step=1))

    st.write(sgg_nms, periods)