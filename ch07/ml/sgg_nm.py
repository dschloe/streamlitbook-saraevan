# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import json
from prophet.serialize import model_from_json

plt.rcParams['font.family'] = "Malgun Gothic"

@st.cache_resource
def load_models(sgg_nms):
    models = []
    for sgg_nm in sgg_nms:
        print(sgg_nm)
        with open(f'ml/models/{sgg_nm}_model.json', 'r') as fin:
            model = model_from_json(json.load(fin))  # Load model
        models.append(model)
    models
    return models

def predictDistrict(total_df):

    total_df['DEAL_YMD'] = pd.to_datetime(total_df['DEAL_YMD'], format="%Y-%m-%d")
    sgg_nms = sorted(list(total_df['SGG_NM'].unique()))
    periods = int(st.number_input("향후 예측 기간을 지정하세요(1일 ~ 30일)", min_value=1, max_value=30, step=1))

    models = load_models(sgg_nms)
    fig, ax = plt.subplots(figsize=(20, 10), sharex=True, sharey=False, ncols=5, nrows=5)
    for i in range(0, len(sgg_nms)):
        future = models[i].make_future_dataframe(periods=periods)
        forecast = models[i].predict(future)
        print(sgg_nms[i])
        if i <= 4:

            fig = models[i].plot(forecast, uncertainty=True, ax=ax[0, i])
            ax[0, i].set_title(f"서울시 {sgg_nms[i]} 평균가격 예측 시나리오 {periods}일간")
            ax[0, i].set_xlabel(f"날짜")
            ax[0, i].set_ylabel(f"평균가격(만원)")
            for tick in ax[0, i].get_xticklabels():
                tick.set_rotation(30)
        elif i <= 9:

            fig = models[i].plot(forecast, uncertainty=True, ax=ax[1, i - 5])
            ax[1, i - 5].set_title(f"서울시 {sgg_nms[i]} 평균가격 예측 시나리오 {periods}일간")
            ax[1, i - 5].set_xlabel(f"날짜")
            ax[1, i - 5].set_ylabel(f"평균가격(만원)")
            for tick in ax[1, i - 5].get_xticklabels():
                tick.set_rotation(30)
        elif i <= 14:

            fig = models[i].plot(forecast, uncertainty=True, ax=ax[2, i - 10])
            ax[2, i - 10].set_title(f"서울시 {sgg_nms[i]} 평균가격 예측 시나리오 {periods}일간")
            ax[2, i - 10].set_xlabel(f"날짜")
            ax[2, i - 10].set_ylabel(f"평균가격(만원)")
            for tick in ax[2, i - 10].get_xticklabels():
                tick.set_rotation(30)
        elif i <= 19:

            fig = models[i].plot(forecast, uncertainty=True, ax=ax[3, i - 15])
            ax[3, i - 15].set_title(f"서울시 {sgg_nms[i]} 평균가격 예측 시나리오 {periods}일간")
            ax[3, i - 15].set_xlabel(f"날짜")
            ax[3, i - 15].set_ylabel(f"평균가격(만원)")
            for tick in ax[3, i - 15].get_xticklabels():
                tick.set_rotation(30)
        elif i <= 24:

            fig = models[i].plot(forecast, uncertainty=True, ax=ax[4, i - 20])
            ax[4, i - 20].set_title(f"서울시 {sgg_nms[i]} 평균가격 예측 시나리오 {periods}일간")
            ax[4, i - 20].set_xlabel(f"날짜")
            ax[4, i - 20].set_ylabel(f"평균가격(만원)")
            for tick in ax[4, i - 20].get_xticklabels():
                tick.set_rotation(30)
        else:
            pass

    fig.tight_layout()
    fig.subplots_adjust(top=0.95)
    st.pyplot(fig)
