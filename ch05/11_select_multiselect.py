# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns

# 데이터 불러오기
iris = sns.load_dataset('iris')

def main():

    st.markdown("## Raw Data")
    st.dataframe(iris)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("## Select")
    column = st.selectbox("1개의 종을 선택하세요", iris.species.unique())
    st.dataframe(iris[iris['species']==column].reset_index())

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("## MultiSelect")
    cols = st.multiselect("복수의 컬럼을 선택하세요", iris.columns)
    filtered_iris = iris.loc[:, cols]
    st.dataframe(filtered_iris)

if __name__ == "__main__":
    main()