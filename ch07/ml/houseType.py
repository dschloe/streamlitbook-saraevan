# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from prophet import Prophet

def predict_plot(total_df, types, periods):
    fig, ax = plt.subplots(figsize=(10, 6), sharex=True, ncols=2, nrows=2)
    for i in range(0, len(types)):
        model = Prophet()
        total_df2 = total_df.loc[total_df['HOUSE_TYPE'] == types[i], ["DEAL_YMD", "OBJ_AMT"]]
        result_df = total_df2.groupby('DEAL_YMD')['OBJ_AMT'].agg("mean").reset_index()
        result_df = result_df.rename(columns={"DEAL_YMD": "ds", "OBJ_AMT": "y"})
        model.fit(result_df)
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
        if i <= 1:
            fig = model.plot(forecast, uncertainty=True, ax=ax[0, i])
            ax[0, i].set_title(f"서울시 {types[i]} 평균가격 예측 시나리오 {periods}일간")
            ax[0, i].set_xlabel(f"날짜")
            ax[0, i].set_ylabel(f"평균가격(만원)")
            for tick in ax[0, i].get_xticklabels():
                tick.set_rotation(30)
        else:
            fig = model.plot(forecast, uncertainty=True, ax=ax[1, i-2])
            ax[1, i-2].set_title(f"서울시 {types[i]} 평균가격 예측 시나리오 {periods}일간")
            ax[1, i-2].set_xlabel(f"날짜")
            ax[1, i-2].set_ylabel(f"평균가격(만원)")
            for tick in ax[1, i-2].get_xticklabels():
                tick.set_rotation(30)
    return fig

def predictType(total_df):

    total_df['DEAL_YMD'] = pd.to_datetime(total_df['DEAL_YMD'], format="%Y-%m-%d")
    types = list(total_df['HOUSE_TYPE'].unique())
    periods = int(st.number_input("향후 예측 기간을 지정하세요(1일 ~ 30일)", min_value=1, max_value=30, step=1))

    fig = predict_plot(total_df, types, periods)
    st.pyplot(fig)
    st.markdown("<hr>", unsafe_allow_html=True)







