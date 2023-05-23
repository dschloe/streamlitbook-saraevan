# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from prophet import Prophet
import json
from prophet.serialize import model_from_json
from prophet.plot import plot_plotly
@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

def reportMain(total_df):
    sgg_nm = st.sidebar.selectbox("자치구", sorted(total_df['SGG_NM'].unique()))
    periods = int(st.sidebar.number_input("향후 예측 기간을 지정하세요(1일 ~ 30일)", min_value=1, max_value=30, step=1))

    with open(f'ml/models/{sgg_nm}_model.json', 'r') as fin:
        model = model_from_json(json.load(fin))
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    output = convert_df(forecast)
    st.sidebar.download_button(
        "결과 다운로드(CSV)",
        output,
        f"{sgg_nm}_아파트 평균값 예측 {periods}일간.csv",
        "text/csv",
        key='download-csv'
    )


    fig = plot_plotly(model, forecast)
    fig.update_layout(
        title=dict(text=f"{sgg_nm} 아파트 평균값 예측 {periods}일간",
                   font=dict(size=20),
                   automargin=True,
                   yref='paper'),
        xaxis_title="날짜",
        yaxis_title="아파트 평균값(만원)",
        autosize=False,
        width=700,
        height=800,
    )
    fig.update_yaxes(tickformat='000')
    st.plotly_chart(fig)
