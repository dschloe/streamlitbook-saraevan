# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

import pingouin as pg
import streamlit
from pingouin import ttest

import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st

def twoMeans(total_df):
    total_df['month'] = total_df['DEAL_YMD'].dt.month
    apt_df = total_df[(total_df['HOUSE_TYPE'] == '아파트') & (total_df['month'].isin([3, 4]))]
    st.markdown("### 집계 \n"
                "- 3월과 4월의 아파트 가격을 비교한다.")
    ttest_df = round(apt_df.groupby('month')['OBJ_AMT'].agg(["mean", "std", "size"]), 1)
    st.dataframe(ttest_df, use_container_width=True)

    st.markdown("###  서울시 통합 3월 vs 4월 차이 검정\n"
                "- 3월과 4월의 아파트 평균 가격의 차이를 검정한다. \n"
                "- 가설설정 \n"
                "   + 귀무가설 : $H_{0}$: 3월과 4월의 아파트 평균 차이는 없다. \n"
                "   + 대립가설 : $H_{1}$: 3월과 4월의 아파트 평균 차이는 있다. \n")

    march_df = apt_df[apt_df['month'] == 3]
    april_df = apt_df[apt_df['month'] == 4]
    result = ttest(march_df['OBJ_AMT'], april_df['OBJ_AMT'], paired=False)
    st.dataframe(result, use_container_width=True)
    st.markdown(f"- 확인결과 p-value 값이 {result['p-val'].values[0]} 이므로 $H_{0}$을 채택하여, 3월과 4월의 아파트 평균 차이는 없다.")

    selected_sgg_nm = st.sidebar.selectbox("자치구명", sorted(total_df['SGG_NM'].unique()))
    st.markdown(f"### 서울시 {selected_sgg_nm} 3월 vs 4월 차이 검정\n"
                "- 자치구를 선택하여 3월과 4월의 아파트 평균 차이가 있는지 확인하도록 한다.")

    sgg_df = apt_df[apt_df['SGG_NM'] == selected_sgg_nm]
    sgg_march_df = sgg_df[sgg_df['month'] == 3]
    sgg_april_df = sgg_df[sgg_df['month'] == 4]
    sgg_result = ttest(sgg_march_df['OBJ_AMT'], sgg_april_df['OBJ_AMT'], paired=False)
    st.dataframe(sgg_result, use_container_width=True)
    if sgg_result['p-val'].values[0] > 0.05:
        st.markdown(f"- 확인결과 p-value 값이 {sgg_result['p-val'].values[0]} 이므로 $H_{0}$을 채택하여, 3월과 4월의 아파트 평균 차이는 없다.")
    else:
        st.markdown(f"- 확인결과 p-value 값이 {sgg_result['p-val'].values[0]} 이므로 $H_{1}$을 채택하여, 3월과 4월의 아파트 평균 차이는 있다.")

    st.markdown(f"### 서울시 :blue[{selected_sgg_nm}] 3월 vs 4월 시각화", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 3))
    sns.pointplot(x='month', y='OBJ_AMT', data=sgg_df)
    sns.despine()
    st.pyplot(fig)
    st.dataframe(round(sgg_df.groupby('month')['OBJ_AMT'].agg(["mean", "std", "size"]), 1), use_container_width=True)

def showStat(total_df):
    total_df['DEAL_YMD'] = pd.to_datetime(total_df['DEAL_YMD'], format="%Y-%m-%d")
    selected = st.sidebar.selectbox("분석 메뉴", ['두 집단간 차이 검정', '상관분석', '회귀분석'])
    if selected == '두 집단간 차이 검정':
        st.markdown("### 두 집단간 차이 검정 이론 설명 \n"
                    "- t-검정은 두 개의 독립적인 데이터 샘플의 평균 간에 유의미한 차이가 있는지 확인하는 데 사용할 수 있는 통계 테스트입니다. \n"
                    "- 추가 설명")
        st.markdown("t-통계량을 구하는 것은 아래와 같습니다.")
        st.latex(r'''
        t = \frac{{\bar{X} - \mu}}{{s/\sqrt{n}}}
        ''')
        st.markdown("- $\={X}$ : 표본의 평균을 말합니다. \n"
                    "- LaTeX expressions, by wrapping them in `$` or `$$` (the `$$` must be on their own lines). Supported LaTeX functions are listed at https://katex.org/docs/supported.html. \n"
                    "- 나머지를 추가해보세요.. ")

        twoMeans(total_df)

    elif selected == '상관분석':
        st.markdown("### 상관분석 이론 설명")
    elif selected == "회귀분석":
        st.markdown("### 회귀분석 이론 설명")